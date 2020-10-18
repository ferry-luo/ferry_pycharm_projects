#encoding:utf-8
import time

now_time = str(time.time()) #time()返回当前时间的时间戳（1970纪元后经过的浮点秒数）
print(now_time)
ntime = now_time.split(".")
print(ntime)
n_time = int(ntime[0])
print(n_time)

event_time  = "2020-06-26 10:00:00.000000"
print(event_time)
etime = event_time.split(".")
print(etime)
timeArray = time.strptime(etime[0],"%Y-%m-%d %H:%M:%S") #strptime()返回struct_time对象
print(type(timeArray))
print(timeArray)
e_time = int(time.mktime(timeArray))    #mktime()方法接收struct_time对象作为参数,返回用秒数来表示时间的浮点数
print(e_time)
time_strp = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)    #strftime()返回以可读字符串表示的时间
print(time_strp)