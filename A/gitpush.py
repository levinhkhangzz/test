import os
import threading
import time

# Hàm để thực thi lệnh git push origin main
def push_to_main():
    while True:
        os.system('git push origin main')
        time.sleep(0.1)

# Tạo một luồng để chạy hàm push_to_main
thread = threading.Thread(target=push_to_main)
thread.start()

# Chờ luồng kết thúc (trong trường hợp này, mã này sẽ chạy vô hạn)
thread.join()
