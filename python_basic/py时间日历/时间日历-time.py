# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 0:15:14

import time

# 获取时间戳
# res = time.time()
# years = res / (365 * 24 * 60 * 60) + 1970
# print(res)
# print(years)

# 获取时间元组，可以不传人参数，默认当前时间元组
# res = time.localtime(1564727544.8498905)
# print(res)

# 时间戳获取格式化时间
# t = time.time()
# 格式化时间
# res = time.ctime(t)
# print(res)
# 默认当前时间戳
# res3 = time.ctime()
# print(res3)

# 时间元组获取格式化时间
# time_tuple = time.localtime()
# 格式化时间
# res1 = time.asctime(time_tuple)
# print(res1)
# 默认当前时间元组
# res2 = time.asctime()
# print(res2)

# 时间元组--》格式化日期
# 2022-10-03 09:48:37
# format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 22-10-03 09:49:13
# format_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
# print(format_time)
'''
|符号|	说明|
|%a|	当前区域设置下星期简写，如星期二Tue。|
|%A|	当前区域设置下星期全名，如星期二Tuesday。|
|%b|	当前区域设置下月份简写，如九月Sep。|
|%B|	当前区域设置下月份全名，如九月September。|
|%c|	当前区域设置下的日期和时间表示。|
|%C|	世纪，如2019年，21世纪，则返回20。|
|%d|	十进制数字表示的月份的某一天，范围[01,31]。|
|%D|	日期，等效于“%m/%d/%y”（美国格式），如“09/03/19”|
|%e|	十进制数字表示的月份的某一天，范围[1,31]。如果小时10，则数字前用一个填充一个空格。|
|%F|	ISO 8601格式的完整日期，等效于“%Y-%m-%d”，如“2019-09-03”。|
|%g|	ISO周数对应的不包含世纪的年份，等效于“%y”，除非ISO周数属于前一年或后一年，则使用前一年或后一年，范围[00,99]。|
|%G|	ISO周数对应的年份，等效于“%Y”，除非ISO周数属于前一年或后一年，则使用前一年或后一年，范围[0000,9999]。|
|%h|	等效于“%b”。|
|%j|	十进制表示的在一天中的天数，范围[001,366]。|
|%m|	十进制表示的月份，范围[01,12]。|
|%u|	十进制表示的星期，范围[1-7]。周一为一周的第一天。周一为1，依次递增。|
|%U|	十进制表示的一年中的周数，[00,53]。星期日为一周的第一天，新年第一个星期日之前的所有日子都视为第0周。|
|%V|	十进制表示的一年中的ISO周数，[01,53]。星期一为一周的第一天，如果包含1月1日的一周在新的一年里有四天或四天以上，则认为这周是第一周，否则就是前一年的第53周，下一周是新年的第一周。|
|%w|	十进制表示的星期，范围[0-6]。周日为一周的第一天。周日为0，依次递增。|
|%W|	十进制表示的一年中的周数，[00,53]。星期一为一周的第一天，新年第一个星期一之前的所有日子都视为第0周。|
|%x|	按当前区域设置下的日期格式，如“09/03/19”。|
|%y|	年份的后两位，范围[00,99]。|
|%Y|	年份，范围[0000,9999]。|
'''

'''
时间格式符
符号	说明
|%H|	十进制数字表示的小时（24小时制），范围[00,23]。|
|%I（大写i）|	十进制数字表示的小时（12小时制），范围[01,12]。|
|%M|	分钟，范围[00,59]。|
|%p|	本地区域设置下等价于“AM”或“PM”，在许多地区是空字符串。中午视为“PM”，午夜视为“AM”。|
|%r|	本地区域设置下12小时制时间，如02:15:11 PM。|
|%R|	24小时制的时和分，等效于“%H%M”，如“14:16”。|
|%S|	十进制数字表示的秒，范围[00,61]。60在表示闰秒的时间戳中有效，61是出于历史原因而支持的。|
|%T|	24小时制的时分秒，等效于“%H:%M:%S”。|
|%X|	按当前区域设置下的日期格式，如“02:20:24 PM”。|
|%z|	表示与UTC/GMT的正或负时差的时区偏移量，格式为+HHMM或-HHMM，其中H表示小时数，M表示分钟数，范围是[-23:59,+23:59]。|
|%Z|	时区名。没有时区则返回空字符。|
'''

# format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(format_time)
# 格式化时间--》时间元组  time.strptime(日期字符串, 格式符字符串)
# time.struct_time(tm_year=2022, tm_mon=10, tm_mday=3, tm_hour=10, tm_min=3, tm_sec=41, tm_wday=0, tm_yday=276, tm_isdst=-1)
# pt = time.strptime("2022-10-03 10:03:41", "%Y-%m-%d %H:%M:%S")
# print(pt)

# 通过时间元组时间戳
# time_mktime = time.mktime(pt)
# print(time_mktime)

# 获取当前cpu时间
# python3.8后不支持time.clock(),使用time.perf_counter()代替
# startClock = time.clock()
# startClock = time.perf_counter()
# for i in range(0, 1000):
    # print(i)
# endClock = time.clock()
# endClock = time.perf_counter()
# print(endClock-startClock)

# 休眠时间，让线程暂停sec秒  time.sleep(sec)
while True:
    format_time = time.strftime(" %Y-%m-%d  %H:%M:%S ", time.localtime())
    print(format_time)
    time.sleep(1)

