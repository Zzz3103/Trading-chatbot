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

if __name__ == "__main__":
    input_file = "data/data-20250723T011529Z-1-001/data/news.csv"
    result = convert_to_markdown(input_file)
    print(result[:500])
