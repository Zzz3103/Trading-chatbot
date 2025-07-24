import os
import hashlib
from markitdown import MarkItDown
from jinja2 import Template


def hash_directory(path, exclude_file=None):
    sha256 = hashlib.sha256()

    for root, dirs, files in os.walk(path):
        files.sort()  # Đảm bảo thứ tự cố định
        for file in files:
            if exclude_file and file == exclude_file:
                continue  # Bỏ qua file được loại trừ

            file_path = os.path.join(root, file)
            sha256.update(file_path.encode())  # Thêm đường dẫn

            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)  # Thêm nội dung

    return sha256.hexdigest()

def get_files_in_directory(path):
    files = []
    for f in os.listdir(path):
        path_f = os.path.join(path, f)
        if os.path.isfile(path_f):
            files.append(path_f)
        elif os.path.isdir(path_f):
            files.extend(get_files_in_directory(path_f))

    return files

def convert_to_markdown(path: str) -> str:
    # Khởi tạo converter
    converter = MarkItDown()

    # Chuyển file sang markdown
    result = converter.convert(path)

    return result.markdown


def has_hash_changed(path: str) -> bool:
    # Hash toàn bộ thư mục data
    old_hash = ""
    old_hash_file = os.path.join(path, "hash.hsh")
    if os.path.exists(old_hash_file):
        with open(old_hash_file, "r") as f:
            old_hash = f.read().strip()

    hash = hash_directory(path, "hash.hsh")

    if old_hash == hash:
        return False

    with open(old_hash_file, "w") as f:
        f.write(hash)

    return True


def render_prompt(template_path, docs, question):
    with open(template_path, "r", encoding="utf-8") as f:
        template_str = f.read()
    template = Template(template_str)
    return template.render(docs=docs, question=question)

if __name__ == "__main__":
    from index_data import Vector_Store

    vector_store = Vector_Store()
    index_data = vector_store.index_data(path="data")
    question = "HPG thuộc xu hướng nào"
    docs = vector_store.search(query=question, top_k = 5)
    docs = [doc for doc in docs if doc.metadata["score"] >= 0.1]
    prompt = render_prompt("templates/prompt.txt", docs, question=question)

    print(prompt)

    # from langchain.schema import Document
    # from langchain.text_splitter import RecursiveCharacterTextSplitter
  
    # text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    #         chunk_size=512, chunk_overlap=126
    #     )

    # m = convert_to_markdown("/home/khai/Trading-chatbot/data/data-20250723T011529Z-1-001/data/stockcode_data/dsc_text_files/HPG – MUA.txt")
    # docs = [Document(page_content=m)]
    # chunk_contents = text_splitter.transform_documents(docs)
    # chunk_contents = ["Nguồn: " + '\n' + doc.page_content.replace("\n", " ") for doc in chunk_contents]
    # for i in range(len(chunk_contents)):
    #     print(f"Chunk {i}: {chunk_contents[i]}")
