# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 12:00:11

def mysum(a, b):
    return a + b

def cal(a, b):
    """
    计算两个数值的和
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，不可选，没有默认值，元组(和, 差)
    :return: 两个数值的和和差
    """
    he = a + b
    cha = a - b
    return (he, cha)


print(mysum(1, 2))
he, cha = cal(4, 2)
print(he, cha)
# 函数说明
help(cal)