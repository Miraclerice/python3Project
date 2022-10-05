# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 15:15:19

# 匿名函数
res = (lambda x, y: x + y)(1, 2)
print(res)

func = lambda x, y: x + y
print(func(1, 2))

l = [{"name": "ssd1", "age": 15}, {"name": "ssd4", "age": 125}, {"name": "ssd2", "age": 25},
     {"name": "ssd3", "age": 18}, {"name": "ssd5", "age": 14}]

# def getKey(dic):
#      return dic["name"]

l1 = sorted(l, key=lambda dic: dic["age"])
print(l1)
