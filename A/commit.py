import datetime
import os
import random
import threading

# Hàm thực hiện việc tạo commit
def create_commits(res_date):
    for i in range(random.randrange(1, 10023842384723842748)):
        with open('change-file.txt', 'a') as wf:
            wf.write(f'\n{res_date}')
        os.system(f'git add .')
        os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')

# Hàm chính để chạy các công việc trong các luồng riêng biệt
def main():
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    last_year = current_year - 0
    last_month = today.month
    last_day = current_day - 0  # In case it is a leap year

    start = datetime.date(last_year, last_month, last_day)
    end = datetime.date(current_year, current_month, current_day)
    res_date = start

    while res_date <= end:
        # Tạo một luồng mới cho mỗi ngày và thực hiện tạo commit
        thread = threading.Thread(target=create_commits, args=(res_date,))
        thread.start()
        res_date += datetime.timedelta(days=1)

# Gọi hàm main để bắt đầu thực hiện công việc
main()
