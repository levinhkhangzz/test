import os
import threading
import uuid

def create_empty_directory(directory_name):
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        pass

def create_directories():
    while True:
        threads = []
        for _ in range(50):
            directory_name = str(uuid.uuid4())[:8]  # Tạo một tên thư mục ngẫu nhiên từ uuid và chỉ lấy 8 ký tự đầu
            thread = threading.Thread(target=create_empty_directory, args=(directory_name,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    create_directories()
