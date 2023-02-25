import datetime
import os
import random
import time

try:
    count = 0
    while True: 
        # Chỉnh sửa ngày tháng bắt đầu và kết thúc ở đây
        start_date = datetime.date(2023, 1, 1)  # Ngày bắt đầu: 1/1/2023
        end_date = datetime.date(2024, 2, 17)    # Ngày kết thúc: 17/2/2024

        # Bốc ngẫu nhiên một ngày từ khoảng từ start_date đến end_date
        random_date = datetime.date(random.randint(start_date.year, end_date.year), 
                                    random.randint(1, 12), 
                                    random.randint(1, 28))  # Giả sử mỗi tháng có tối đa 28 ngày để đảm bảo không có lỗi ngày không tồn tại

        while random_date <= end_date:
            for i in range(random.randrange(1, 6111111111)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{random_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{random_date}" -m "#{i} commit for {random_date}"')
                count += 1
                if count >= 5000000:
                    raise StopIteration  

            # Bốc ngẫu nhiên một ngày mới
            random_date = datetime.date(random.randint(start_date.year, end_date.year), 
                                        random.randint(1, 12), 
                                        random.randint(1, 28))

        time.sleep(1)  # Chạy lại sau 1 giây nếu có lỗi
except StopIteration:
    print("Success")
except KeyboardInterrupt:
    print("STOPPED BY USER")
