from index_data import Vector_Store
from chat import ask_llm
import pandas as pd


def main():
    vector_store = Vector_Store()
    vector_store.index_data(path="data")

    # đọc file xlxs
    df = pd.read_excel("test_question.xlsx")

    # duyệt từng dòng
    answers = []
    for index, row in df.iterrows():
        question = row['inputs']
        context = vector_store.search(query=question, top_k=3)
        context = ""
        for text, score in context:
            context += str(text) + "\n"
        answer = ask_llm(context + question)
        answers.append(answer)
        print("=====================================")
        print(f"Question: {question}")
        print(answer)

    df['answer'] = answers 

    # ghi vào file csv
    df.to_csv("answers.csv", index=False)

if __name__ == "__main__":
    main()