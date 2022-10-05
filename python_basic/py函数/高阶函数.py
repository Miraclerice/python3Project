# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 14:45:41

# 高阶函数
l = [{"name": "ssd1", "age": 15}, {"name": "ssd4", "age": 125}, {"name": "ssd2", "age": 25},
     {"name": "ssd3", "age": 18}, {"name": "ssd5", "age": 14}]


# def getKey(dic):
#      return dic["name"]
#
#
# l1 = sorted(l, key=getKey)
# print(l1)

# 自定义高阶函数
def calculate(num1, num2, calculateFunc):
    return calculateFunc(num1, num2)


def addFunc(num1, num2):
    return num1 + num2


def subFunc(num1, num2):
    return num1 - num2


print(calculate(3, 2, addFunc))
print(calculate(3, 2, subFunc))
