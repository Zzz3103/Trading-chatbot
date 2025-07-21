import hashlib
import os

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
