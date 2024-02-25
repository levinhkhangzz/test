import time
import subprocess

def change_between_zeros_and_ones(line):
    new_line = ""
    for char in line:
        if char == "0":
            new_line += "1"
        elif char == "1":
            new_line += "0"
        else:
            new_line += char
    return new_line

filename = 'change-file.txt'

with open(filename, 'r') as file:
    line = file.readline().strip()

while True:
    with open(filename, 'r+') as file:
        content = file.read()
        file.seek(0)
        modified_line = change_between_zeros_and_ones(line)
        file.write(modified_line)
        file.truncate()
        
    # Thực hiện git add và git commit
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update file.txt"])

    time.sleep(0.1)  # Cân nhắc thời gian chờ tùy thuộc vào tốc độ yêu cầu của bạn
