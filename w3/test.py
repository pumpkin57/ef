# -*- coding:utf-8 -*-
# @Date: 2018/8/31 16:26
# @Author: Cathy.cui
# @File: test.py
import time

def get_times():
    Times = []
    with open("july.txt", "r", encoding='utf-8') as f:
        data = eval(f.read())
        Time = data[0].get("Time")
        Times.append(Time)
        for i in data:
            if i.get("Time") != Time:
                Time = i.get("Time")
                Times.append(Time)
        return Times


def diff(Times):
    Time = 0
    days = int(len(Times)/2)
    print("出勤：%d天" %days)
    for i in range(days):
        if i%2 == 0:
            a = time.mktime(time.strptime(Times[i], '%Y-%m-%dT%H:%M:%S'))
        else:
            b = time.mktime(time.strptime(Times[i], '%Y-%m-%dT%H:%M:%S'))
            Time += (b-a)
    hours = (Time/days)/3600
    print("平均每天出勤时长：%.2f小时" %hours)


if __name__ == '__main__':
    Times = get_times()
    diff(Times)



