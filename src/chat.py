from langchain_ollama import OllamaLLM 


OLLAMA_BASE_URL = "http://localhost:11434"

model = OllamaLLM(model="qwen3:4b", base_url=OLLAMA_BASE_URL, temperature=0, reasoning=False)


def ask_llm(prompt):
    system_prompt = ""
    for chunk in model.stream(prompt):
        yield chunk

    # return model.invoke(prompt)




if __name__ == "__main__":
    # question = "Giới thiệu ngắn về mô hình ngôn ngữ lớn là gì?"
    # for chunk in ask_llm(question):
    #     print(chunk, end='')



    question = """
    aah
{'nhomNganh': 'Nguyên vật liệu; Nguyên vật liệu; Hóa chất', 'ket_qua_kinh_doanh': 'Kết quả kinh doanh, Năm 2021 Doanh thu thuần 13,143,110, Lợi nhuận gộp 1,301,375, LN thuần từ HĐKD 405,102, LNST thu nhập DN 324,143, LNST của CĐ cty mẹ 290,241; Kết quả kinh doanh, Năm 2022 Doanh thu thuần 15,290,297, Lợi nhuận gộp 1,086,240, LN thuần từ HĐKD 187,294, LNST thu nhập DN 117,291, LNST của CĐ cty mẹ 152,599; Kết quả kinh doanh, Năm 2023 Doanh thu thuần 12,621,514, Lợi nhuận gộp 1,108,693, LN thuần từ HĐKD 368,684, LNST thu nhập DN 309,194, LNST của CĐ cty mẹ 289,411; Kết quả kinh doanh, Năm 2024 Doanh thu thuần 12,782,231, Lợi nhuận gộp 1,484,106, LN thuần từ HĐKD 513,663, LNST thu nhập DN 319,782, LNST của CĐ cty mẹ 368,581', 'can_doi_ke_toan': 'Cân đói kế toán, Năm 2021 Tài sản ngắn hạn 5,354,611, Tổng tài sản 10,009,527, Nợ phải trả 4,555,145, Nợ ngắn hạn 3,282,339, Vốn chủ sở hữu 5,454,382; Cân đói kế toán, Năm 2022 Tài sản ngắn hạn 5,658,759, Tổng tài sản 10,795,833, Nợ phải trả 4,624,647, Nợ ngắn hạn 3,206,483, Vốn chủ sở hữu 6,171,185; Cân đói kế toán, Năm 2023 Tài sản ngắn hạn 5,681,580, Tổng tài sản 11,583,446, Nợ phải trả 5,619,575, Nợ ngắn hạn 3,737,041, Vốn chủ sở hữu 5,963,871; Cân đói kế toán, Năm 2024 Tài sản ngắn hạn 6,426,369, Tổng tài sản 13,768,216, Nợ phải trả 7,531,942, Nợ ngắn hạn 4,132,594, Vốn chủ sở hữu 6,236,274', 'chi_so_tai_chinh': 'Chỉ số tài chính, Năm 2021 EPS 4 quý 1,042.00, BVPS cơ bản 16,709.00, P/E cơ bản 19.39, ROS 2.47, ROEA 6.12, ROAA 3.12; Chỉ số tài chính, Năm 2022 EPS 4 quý 432.00, BVPS cơ bản 16,143.00, P/E cơ bản 15.79, ROS 0.77, ROEA 2.63, ROAA 1.47; Chỉ số tài chính, Năm 2023 EPS 4 quý 757.00, BVPS cơ bản 15,601.00, P/E cơ bản 12.48, ROS 2.45, ROEA 4.77, ROAA 2.59; Chỉ số tài chính, Năm 2024 EPS 4 quý 964.00, BVPS cơ bản 16,314.00, P/E cơ bản 9.04, ROS 2.50, ROEA 6.04, ROAA 2.91'}
{'nhomNganh': 'Năng lượng; Năng lượng; Dầu khí', 'ket_qua_kinh_doanh': 'Kết quả kinh doanh, Năm 2021 Doanh thu thuần 452,388, Lợi nhuận gộp 34,190, LN thuần từ HĐKD -13,193, LNST thu nhập DN -17,038, LNST của CĐ cty mẹ -17,038; Kết quả kinh doanh, Năm 2022 Doanh thu thuần 591,879, Lợi nhuận gộp 151,627, LN thuần từ HĐKD 115,695, LNST thu nhập DN 101,865, LNST của CĐ cty mẹ 101,865; Kết quả kinh doanh, Năm 2023 Doanh thu thuần 232,366, Lợi nhuận gộp 37,841, LN thuần từ HĐKD 16,846, LNST thu nhập DN 11,642, LNST của CĐ cty mẹ 11,642; Kết quả kinh doanh, Năm 2024 Doanh thu thuần 1,172,122, Lợi nhuận gộp 54,782, LN thuần từ HĐKD 40,498, LNST thu nhập DN 11,945, LNST của CĐ cty mẹ 11,945', 'can_doi_ke_toan': 'Cân đói kế toán, Năm 2021 Tài sản ngắn hạn 576,214, Tổng tài sản 1,283,468, Nợ phải trả 217,749, Nợ ngắn hạn 215,501, Vốn chủ sở hữu 1,065,719; Cân đói kế toán, Năm 2022 Tài sản ngắn hạn 498,312, Tổng tài sản 1,297,533, Nợ phải trả 129,950, Nợ ngắn hạn 128,102, Vốn chủ sở hữu 1,167,584; Cân đói kế toán, Năm 2023 Tài sản ngắn hạn 419,026, Tổng tài sản 1,324,072, Nợ phải trả 144,847, Nợ ngắn hạn 143,472, Vốn chủ sở hữu 1,179,226; Cân đói kế toán, Năm 2024 Tài sản ngắn hạn 418,393, Tổng tài sản 1,455,151, Nợ phải trả 263,981, Nợ ngắn hạn 263,030, Vốn chủ sở hữu 1,191,170', 'chi_so_tai_chinh': 'Chỉ số tài chính, Năm 2021 EPS 4 quý -145.00, BVPS cơ bản 9,039.00, P/E cơ bản 0, ROS -3.77, ROEA -2.57, ROAA -1.37; Chỉ số tài chính, Năm 2022 EPS 4 quý 864.00, BVPS cơ bản 9,903.00, P/E cơ bản 0, ROS 17.21, ROEA 9.12, ROAA 7.89; Chỉ số tài chính, Năm 2023 EPS 4 quý 99.00, BVPS cơ bản 10,002.00, P/E cơ bản 0, ROS 5.01, ROEA 0.99, ROAA 0.89; Chỉ số tài chính, Năm 2024 EPS 4 quý 101.00, BVPS cơ bản 10,103.00, P/E cơ bản 35.53, ROS 1.02, ROEA 1.01, ROAA 0.86'}
{'nhomNganh': 'Công nghiệp; Vận tải; Vận tải biển', 'ket_qua_kinh_doanh': 'Kết quả kinh doanh, Năm 2021 Doanh thu thuần 1,955,301, Lợi nhuận gộp 714,294, LN thuần từ HĐKD 641,928, LNST thu nhập DN 550,615, LNST của CĐ cty mẹ 445,513; Kết quả kinh doanh, Năm 2022 Doanh thu thuần 3,205,610, Lợi nhuận gộp 1,421,745, LN thuần từ HĐKD 1,299,698, LNST thu nhập DN 1,040,793, LNST của CĐ cty mẹ 821,937; Kết quả kinh doanh, Năm 2023 Doanh thu thuần 2,612,690, Lợi nhuận gộp 611,066, LN thuần từ HĐKD 447,055, LNST thu nhập DN 357,825, LNST của CĐ cty mẹ 384,901; Kết quả kinh doanh, Năm 2024 Doanh thu thuần 3,992,095, Lợi nhuận gộp 1,266,706, LN thuần từ HĐKD 980,436, LNST thu nhập DN 800,226, LNST của CĐ cty mẹ 650,499', 'can_doi_ke_toan': 'Cân đói kế toán, Năm 2021 Tài sản ngắn hạn 1,287,238, Tổng tài sản 3,232,345, Nợ phải trả 1,330,315, Nợ ngắn hạn 620,604, Vốn chủ sở hữu 1,902,030; Cân đói kế toán, Năm 2022 Tài sản ngắn hạn 1,744,507, Tổng tài sản 5,049,419, Nợ phải trả 2,162,499, Nợ ngắn hạn 910,335, Vốn chủ sở hữu 2,886,921; Cân đói kế toán, Năm 2023 Tài sản ngắn hạn 1,600,184, Tổng tài sản 5,358,949, Nợ phải trả 2,188,204, Nợ ngắn hạn 937,259, Vốn chủ sở hữu 3,170,746; Cân đói kế toán, Năm 2024 Tài sản ngắn hạn 1,752,840, Tổng tài sản 7,289,525, Nợ phải trả 3,317,832, Nợ ngắn hạn 1,210,097, Vốn chủ sở hữu 3,971,693', 'chi_so_tai_chinh': 'Chỉ số tài chính, Năm 2021 EPS 4 quý 9,372.00, BVPS cơ bản 38,990.00, P/E cơ bản 7.24, ROS 28.16, ROEA 27.52, ROAA 16.73; Chỉ số tài chính, Năm 2022 EPS 4 quý 13,156.00, BVPS cơ bản 41,040.00, P/E cơ bản 2.45, ROS 32.47, ROEA 34.33, ROAA 19.85; Chỉ số tài chính, Năm 2023 EPS 4 quý 4,572.00, BVPS cơ bản 30,050.00, P/E cơ bản 8.22, ROS 13.70, ROEA 12.71, ROAA 7.40; Chỉ số tài chính, Năm 2024 EPS 4 quý 5,712.00, BVPS cơ bản 32,731.00, P/E cơ bản 8.67, ROS 20.05, ROEA 18.22, ROAA 10.29'}
"""
    for chunk in ask_llm(question):
        print(chunk, end='')
