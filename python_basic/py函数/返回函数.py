# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 15:04:26

# 返回函数
def getFunc(flag):
    def getAdd(num1, num2, num3):
        return num1 + num2 + num3

    def getSub(num1, num2, num3):
        return num1 - num2 - num3

    # 根据flag值判断返回哪一个函数
    if flag == "+":
        return getAdd
    elif flag == "-":
        return getSub


func = getFunc("+")
print(func, type(func))
print(func(1, 3, 5))
