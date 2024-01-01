import datetime
import os
import random
import time

try:
    count = 0
    while True: 
        # Chỉnh sửa ngày tháng bắt đầu và kết thúc ở đây
        start_date = datetime.date(2024, 1, 1)  # Ngày bắt đầu: 1/1/2022
        end_date = datetime.date(2027, 2, 16)    # Ngày kết thúc: 16/2/2024

        res_date = start_date

        while res_date <= end_date:
            for i in range(random.randrange(1, 6111111111)):
                with open('change-file.txt', 'a') as wf:
                    wf.write(f'\n{res_date}')
                os.system(f'git add .')
                os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
                count += 1
                if count >= 5000000:
                    raise StopIteration  
            res_date += datetime.timedelta(days=1)

        time.sleep(1)  # Chạy lại sau 1 giây nếu có lỗi
except StopIteration:
    print("Success")
except KeyboardInterrupt:
    print("STOPPED BY USER")
