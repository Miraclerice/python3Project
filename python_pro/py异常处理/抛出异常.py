# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 23:56:23

def setAge(age):
    if age <= 0 or age > 200:
        raise ValueError("值错误")
    else:
        print(age)


try:
    setAge(-2)
except Exception as e:
    print(e)
