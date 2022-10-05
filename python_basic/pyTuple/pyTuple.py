# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 19:20:25

t = (1,)
t1 = (1, 2, "jj")
t2 = 1, "hh"
print(type(t))
print(type(t1))
print(type(t2))
# 列表转换成元组
l = ["ss", "ll", "pp"]
changTuple = tuple(l)
print(changTuple, type(changTuple))
t3 = ('gg', t1, t2)
print(t3, type(t3))


