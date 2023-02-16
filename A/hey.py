import os
import random
import threading
import time

# Hàm thực thi để tạo issue
def create_issue():
    while True:
        # Chọn một tiêu đề và nội dung ngẫu nhiên cho issue
        random_title = random.choice(issue_titles)
        random_body = random.choice(issue_bodies)

        # Tạo lệnh để tạo issue
        command = f'gh issue create --title "{random_title}" --body "{random_body}"'

        # Thực thi lệnh
        os.system(command)

        # Tạm dừng chương trình trong một khoảng thời gian ngắn (ví dụ: từ 1 đến 3 giây)
        time.sleep(random.uniform(0, 1))  # Sử dụng uniform để có thời gian chờ ngẫu nhiên

# Tạo danh sách các tiêu đề và nội dung issue có thể sử dụng
issue_titles = ['Bug fix', 'Feature request', 'Documentation update', 'Performance improvement']
issue_bodies = [
    'This is a bug fix for issue #123.',
    'I propose adding a new feature to enhance functionality.',
    'Update documentation to reflect recent changes.',
    'Optimize code for better performance.'
]

# Số lượng luồng bạn muốn chạy
num_threads = 5

# Tạo và khởi động các luồng
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=create_issue)
    thread.start()
    threads.append(thread)

# Chờ tất cả các luồng kết thúc
for thread in threads:
    thread.join()
