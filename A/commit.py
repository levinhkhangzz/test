import datetime
import os
import random
import time  # Import thư viện time để sử dụng hàm sleep

try:
    count = 0
    while True: 
        today = datetime.date.today()

        current_year = today.year
        current_month = today.month
        current_day = today.day

        random_year = random.randint(2023, 2024)
        # Chọn ngẫu nhiên một tháng và một ngày từ 1/1 đến 31/12
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # Giả sử mỗi tháng có tối đa 28 ngày để đảm bảo không có ngày không hợp lệ
# xong rồi anh em tạo chạy file gitpush.py để push code len github để tạo lịch sử commit
        start = datetime.date(random_year, random_month, random_day)
        end = datetime.date(current_year, current_month, current_day)
        res_date = start

        while res_date <= end:
            for i in range(random.randrange(1, 6111111111)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{res_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
                count += 1
                if count >= 5000000:
                    raise StopIteration  
            res_date += datetime.timedelta(days=1)

       
        time.sleep(1) # chỗ này là nếu lỗi nó sẽ tự động chạy lại sau 1 giây
except StopIteration:
    print("Success")
except KeyboardInterrupt:
    print("STOPPED BY USER")