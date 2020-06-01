import time
import datetime

#time模块提供的功能更加接近于操作系统层面，能表述的日期范围在1970-2038之间，此范围之外的则要用datetime模块
def calculate_different_time():
    local_time = time.localtime()
    s_time = time.strftime("%Y-%m-%d %H:%M:%S",local_time)  #变为某种格式的日期，但类型是字符串
    start_time = datetime.datetime.strptime(s_time,"%Y-%m-%d %H:%M:%S") # 转成日期格式
    destination_time = "2020-02-09 23:59:59"
    end_time = datetime.datetime.strptime(destination_time,"%Y-%m-%d %H:%M:%S") # 转成日期格式

    diff_time = end_time - start_time
    print(diff_time)

if __name__ == "__main__":
    calculate_different_time()
