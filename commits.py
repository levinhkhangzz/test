import datetime
import os
import random

while True:
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    last_year = current_year - 1
    last_month = today.month
    last_day = current_day - 1  # In case it is a leap year

    start = datetime.date(last_year, last_month, last_day)
    end = datetime.date(current_year, current_month, current_day)
    res_date = start

    with open('change-file.txt', 'r') as f:
        lines = f.readlines()

    if lines:
        lines[0] = str(res_date) + '\n'

        with open('change-file.txt', 'w') as wf:
            wf.writelines(lines)

    for i in range(random.randrange(1, 6)):
        os.system(f'git add .')
        os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')

    res_date += datetime.timedelta(days=1)
