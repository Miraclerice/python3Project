# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 0:02:02

# 数据保护
from typing import Any


class Person:
    # 当我们创建好一个对象后，会自动调用该方法，初始化对象
    def __init__(self):
        self.__age = 18

    def setAge(self, value):
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print("您输入的数值有问题，请重新输入")

    def getAge(self):
        return self.__age


p1 = Person()
# pack1.__age = -10
p1.setAge("aa")
# print(pack1._Person__age)
print(p1.getAge())

p2 = Person()

p3 = Person()

# print(pack1.__dict__)
# print(pack1.__age)
# print(p2.__age)
# print(p3.__age)

# 数据过滤
