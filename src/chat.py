from langchain_ollama import OllamaLLM 


OLLAMA_BASE_URL = "http://localhost:11434"

model = OllamaLLM(model="qwen2.5:7b", base_url=OLLAMA_BASE_URL, temperature=0, reasoning=False)


def ask_llm(prompt):
    system_prompt = (
        "Trả lời câu hỏi của người dùng bằng cách sử dụng các đoạn văn sau; "
        "sử dụng ngôn ngữ tiếng Việt.\n"
    )
    full_prompt = system_prompt + prompt
    return model.invoke(full_prompt)


def ask_llm_stream(prompt):
    system_prompt = (
        "Trả lời câu hỏi của người dùng bằng cách sử dụng các đoạn văn sau; "
        "sử dụng ngôn ngữ tiếng Việt.\n"
    )
    full_prompt = system_prompt + prompt
    for chunk in model.stream(full_prompt):
        yield chunk






if __name__ == "__main__":
    question = "Giới thiệu ngắn về mô hình ngôn ngữ lớn là gì?"
    # for chunk in ask_llm(question):
    #     print(chunk, end='')

    answer = ask_llm(question)
    print(answer)

