# -*- coding: utf-8 -*-
# @Author  : XieBingxian
# @Time    : 2022/8/23/0023 9:59:09
# @File    : demo2.py
# @Software: PyCharm
#
# b = ['jjl', 'kkk', 'kkp']
# print(b[0])
# print(b[0].title())

# bike = []
# bike.append('孙悟空')
# bike.append('唐三藏')
# print(bike)
# bike.insert(1, '沙悟净')
# print(bike)
# bike.sort()
#
# del bike[1]
# # print(bike)
# bike_pop = bike.pop(0)
# print(bike)
# print(bike_pop)


cars = ['baoma', 'fengtian', 'falali', 'dazong']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)  # 逆向排序
# print(cars)
# print(sorted(cars))

print(cars)
cars.reverse()
print(cars)
print(len(cars))


def run():
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)


run();

print(1)

import keyword

print(keyword.kwlist)
a = False
''''''

print(type(a))
print(int('6') + 1)
print(type(int('6')))

print([1, 2] + [3, 4])
print(5 / 2)
print(5.2 // 2)
print(5 / 3)

f, g, h = 1, 2, 3
print(f)

o = 10
o **= 2
print(o)

print(5 < 10 < 11)
print(4 < 10 & 6 < 4)
