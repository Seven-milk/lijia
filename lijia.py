# code: utf-8
# author: "Xudong Zheng" 
# email: Z786909151@163.com
import datetime

# start = datetime.date(2020, 6, 12)
with open('start.text', 'r') as f:
    f_read = f.read().split(',')
    start = datetime.date(int(f_read[0]), int(f_read[1]), int(f_read[2]))

time_delta = datetime.timedelta(days=28)
now = datetime.date.today()
dif = now - start
date = start + ((dif // time_delta) + 1) * time_delta
print("下次例假是：{}".format(date))
# Todo 添加彩蛋
