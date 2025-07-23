import os
import hashlib
from markitdown import MarkItDown

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

    # Chuyển file .docx sang markdown
    result = converter.convert(path)

    return result.markdown



if __name__ == "__main__":
    input_file = "data/QA_STATIC.txt"
    result = convert_to_markdown(input_file)
    print(result)
