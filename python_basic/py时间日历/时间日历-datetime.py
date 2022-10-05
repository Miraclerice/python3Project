# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 10:22:35
import datetime

# 获取当天日期
# datetime_now = datetime.datetime.now()
# print(datetime_now, type(datetime_now))
# print(datetime.datetime.today())
# 单独获取年月日时分秒
# print(datetime_now.year)
# print(datetime_now.month)
# print(datetime_now.day)
# print(datetime_now.hour)
# print(datetime_now.minute)
# print(datetime_now.second)

# t = datetime.datetime.today()
# 计算n天后的日期
# res = t + datetime.timedelta(days=7)
# res = t + datetime.timedelta(days=-7)
# print(t, res)

# 时间间隔
first = datetime.datetime(2020, 12, 26, 10, 30, 10)
second = datetime.datetime(2020, 12, 27, 10, 30, 10)
delta = second - first
# datetime.timedelta 时间间隔类型
print(delta, type(delta))
# 对应的秒数
print(delta.total_seconds())

