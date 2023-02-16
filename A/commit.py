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

        last_year = current_year - 1 #chỗ này trừ 2 là nó sẽ chạy từ 2 năm trước
        last_month = today.month
        last_day = current_day - 1  #chỗ này trừ 1 là nó sẽ chạy từ tháng trước
# xong rồi anh em tạo chạy file gitpush.py để push code len github để tạo lịch sử commit
        start = datetime.date(last_year, last_month, last_day)
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
