import os
import json
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from utils import hash_directory, convert_to_markdown, get_files_in_directory
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Vector_Store:
    def __init__(self, embedding_model_name="intfloat/multilingual-e5-base"):
        local_path = os.path.join("models", embedding_model_name.replace("/", "_"))

        if os.path.exists(local_path):
            print("Loading embedding model from local path...")
            self.embedding_model = SentenceTransformer(local_path)
        else:
            print("Downloading embedding model...")
            self.embedding_model = SentenceTransformer(embedding_model_name)
            self.embedding_model.save(local_path)

        self.qdrant_client = QdrantClient(host="127.0.0.1", port=6333, timeout=600)
        self.collection_name = "local_store"

    def index_data(self, path):
        print(f"Indexing data from {path}...")

        # Hash toàn bộ thư mục data
        old_hash = ""
        old_hash_file = os.path.join(path, "hash.hsh")
        if os.path.exists(old_hash_file):
            with open(old_hash_file, "r") as f:
                old_hash = f.read().strip()

        hash = hash_directory(path, "hash.hsh")

        # Nếu hash không thay đổi thì không cần cập nhật
        if old_hash == hash:
            print("Data has not changed, skipping indexing.")
            return

        with open(old_hash_file, "w") as f:
            f.write(hash)

        # Lấy số chiều của vector từ mô hình embedding
        sample_vector = self.embedding_model.encode("test") 
        dim = sample_vector.shape[0]

        # Tạo mới collection
        self.qdrant_client.recreate_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=dim, distance=Distance.EUCLID),
                )

        idx = 0 
        files = get_files_in_directory(path)
        for f in files:
            if f.endswith(".docx") or f.endswith(".txt"):
                print(f"Processing file: {f}")
                markdown_text = convert_to_markdown(f)
                docs = [Document(page_content=markdown_text)]
                text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                    chunk_size=512, chunk_overlap=126
                )
                text = text_splitter.transform_documents(docs)
            else:
                # Bỏ qua các file khác
                continue
        
            embeddings = self.embedding_model.encode([doc.page_content for doc in text])

            points = [
                PointStruct(
                    id=i + idx,
                    vector=embeddings[i].tolist(),
                    payload={"text": text[i].page_content},
                )
                for i in range(len(text))
            ]
            idx += len(points)

            # Chia nhỏ thành các batch để tránh lỗi quá tải
            BATCH_SIZE = 100
            for i in range(0, len(points), BATCH_SIZE):
                batch = points[i:i + BATCH_SIZE]
                self.qdrant_client.upsert(
                    collection_name=self.collection_name,
                    points=batch
                )
                print(f"Upserted batch {i // BATCH_SIZE + 1} of {len(points) // BATCH_SIZE + 1}")

    def search(self, query, top_k=5):
        query_vector = self.embedding_model.encode([query])[0]

        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_vector.tolist(),
            limit=top_k
        )

        return [(hit.payload["text"], hit.score) for hit in hits]


if __name__ == "__main__":
    vector_store = Vector_Store()
    index_data = vector_store.index_data(path="data")
    context = vector_store.search(query="chứng khoán là gì", top_k = 3)
    for text, score in context:
        print(f"Text: {text}, Score: {score}")
        print("\n")

