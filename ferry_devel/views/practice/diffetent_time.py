#encoding:utf-8
import time
import datetime

#计算时间差
def calculate_different_time():
    local_time = time.localtime()
    current_time = time.strftime("%H:%M:%S",local_time)
    start_time = datetime.datetime.strptime(current_time,"%H:%M:%S")
    destination_time = "23:59:59"
    end_time = datetime.datetime.strptime(destination_time,"%H:%M:%S")
    different_time = end_time - start_time
    print(different_time)

if __name__ == "__main__":
    calculate_different_time()