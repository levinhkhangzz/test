import datetime
import os
import random
import time

try:
    count = 0
    while True: 
        # Chọn ngẫu nhiên một năm từ 2023 đến 2024
        random_year = random.randint(2023, 2024)

        # Chọn ngẫu nhiên một tháng và một ngày từ 1/1 đến 31/12
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # Giả sử mỗi tháng có tối đa 28 ngày để đảm bảo không có ngày không hợp lệ

        # Tạo ngày từ các giá trị ngẫu nhiên đã chọn
        random_date = datetime.date(random_year, random_month, random_day)

        while random_date <= datetime.date(2024, 2, 17):  # Chạy cho đến ngày 17/2/2024
            for _ in range(200):  # Thực hiện 200 commit cho mỗi ngày
                for i in range(random.randrange(1, 6111111111)):
                    with open('change-file.txt', 'a') as wf:
                        wf.write(f'\n{random_date}')
                    os.system(f'git add .')
                    os.system(f'git commit --date "{random_date}" -m "#{i} commit for {random_date}"')
                    count += 1
                    if count >= 5000000:
                        raise StopIteration  
            # Tạo ngày mới ngẫu nhiên
            random_year = random.randint(2023, 2024)
            random_month = random.randint(1, 12)
            random_day = random.randint(1, 28)
            random_date = datetime.date(random_year, random_month, random_day)

        time.sleep(1)  # Chạy lại sau 1 giây nếu có lỗi
except StopIteration:
    print("Success")
except KeyboardInterrupt:
    print("STOPPED BY USER")
