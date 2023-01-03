# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# for local time
import time
lt = time.localtime()
days = lt.tm_mday
years = lt.tm_year
month = lt.tm_mon
hours = lt.tm_hour
min = lt.tm_min
sec = lt.tm_sec
print(days,month,years, sep="/")
print (hours,min,sec,sep=":")