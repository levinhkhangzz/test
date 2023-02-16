import datetime
import os
import random

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

# Open the file outside of the loop
with open('change-file.txt', 'a') as wf:
    while res_date <= end:
        commits = []
        for i in range(random.randrange(1, 6)):
            wf.write(f'\n{res_date}')
            commits.append(f'#{i} commit for {res_date}')

        # Combine all commit messages into a single string
        commit_messages = ' && '.join([f'git commit --date "{res_date}" -m "{message}"' for message in commits])
        
        # Execute the commit commands
        os.system(commit_messages)
        
        res_date += datetime.timedelta(days=1)
