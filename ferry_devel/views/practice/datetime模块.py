#encoding:utf-8
import datetime

today = datetime.date.today()

tomorrow = (today + datetime.timedelta(1)).strftime("%Y%m%d")
yesterday = (today + datetime.timedelta(-1)).strftime("%Y%m%d")

f_today = today.strftime("%Y%m%d %H:%M:%S")

print(yesterday)
print(f_today)
print(tomorrow)
