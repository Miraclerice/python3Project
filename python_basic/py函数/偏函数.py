# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 12:46:55
import functools


def mySum(a, b, c, d=1):
    print(a + b + c + d)


# 偏函数
# def mySum1(a, b, c=1, d=2):
#     mySum(a, b, c, d)
#
# mySum1(1, 2)

newFunc = functools.partial(mySum, c=5)
# print(newFunc, type(newFunc))
# 利用functools.partial(mySum, c=5)生成的偏函数不能多写参数，会报错
# newFunc(1, 2, 3, 4)
# newFunc(1, 2)


numStr = "1000010"
# 二进制转换成十进制
print(int(numStr, base=2))

# 使用偏函数，不用重复写base参数
int2 = functools.partial(int, base=2)
print(int2(numStr))