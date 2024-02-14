import datetime
import os
import random
import time

try:
    count = 0
    while True: 
        # Chỉnh sửa ngày tháng bắt đầu và kết thúc ở đây
        start_date = datetime.date(2023, 1, 1)  # Ngày bắt đầu: 1/1/2022
        end_date = datetime.date(2024, 2, 17)    # Ngày kết thúc: 16/2/2024

        # Bốc ngẫu nhiên một ngày từ khoảng từ start_date đến end_date
        res_date = datetime.date.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))

        while res_date <= end_date:
            for i in range(random.randrange(1, 6111111111)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{res_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
                count += 1
                if count >= 5000000:
                    raise StopIteration  
            res_date = datetime.date.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))  # Bốc ngẫu nhiên một ngày mới

        time.sleep(1)  # Chạy lại sau 1 giây nếu có lỗi
except StopIteration:
    print("Success")
except KeyboardInterrupt:
    print("STOPPED BY USER")
