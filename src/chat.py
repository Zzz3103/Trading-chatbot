from langchain_ollama import OllamaLLM 


OLLAMA_BASE_URL = "http://localhost:11434"

model = OllamaLLM(model="qwen2.5:7b", base_url=OLLAMA_BASE_URL, temperature=0, reasoning=False)


def ask_llm(prompt):
    system_prompt = ""
    for chunk in model.stream(prompt):
        yield chunk

    # return model.invoke(prompt)




if __name__ == "__main__":
    question = "Giới thiệu ngắn về mô hình ngôn ngữ lớn là gì?"
    for chunk in ask_llm(question):
        print(chunk, end='')

