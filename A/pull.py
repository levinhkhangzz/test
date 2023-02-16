import os
import random
import string
import time

# Tạo danh sách các tiêu đề và nội dung thảo luận có thể sử dụng
discussion_titles = ['Feedback on new feature', 'Discuss project roadmap', 'Code review for PR #123', 'Ideas for upcoming release']
discussion_contents = [
    'Please share your thoughts and feedback on the new feature implementation.',
    'Let\'s discuss the roadmap for the project and prioritize upcoming tasks.',
    'This discussion is for reviewing the code changes in pull request #123.',
    'We are gathering ideas and suggestions for the upcoming release. Please contribute!'
]

# Hàm để tạo thảo luận mới
def create_discussion(discussion_title, discussion_content):
    # Tạo lệnh để tạo thảo luận
    command = f'gh discussion create --title "{discussion_title}" --body "{discussion_content}"'

    # Thực thi lệnh
    os.system(command)

# Số lượng thảo luận bạn muốn tạo
num_discussions = 100

# Tạo và thảo luận mới
for _ in range(num_discussions):
    discussion_title = random.choice(discussion_titles)  # Chọn tiêu đề ngẫu nhiên từ danh sách
    discussion_content = random.choice(discussion_contents)  # Chọn nội dung ngẫu nhiên từ danh sách
    create_discussion(discussion_title, discussion_content)

    time.sleep(1)  # Đợi 1 giây giữa mỗi lần tạo thảo luận để tránh gây ra quá tải cho máy chủ GitHub
