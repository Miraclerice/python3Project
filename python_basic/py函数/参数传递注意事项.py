# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 11:50:22

# def myfun(num):
#     print("函数内：")
#     # 2568417465808
#     print(num, id(num))
#     # 不可变类型改变不了原件，此时的num是新开辟的空间568417465840
#     num = 101
#     print(num, id(num))
#
#
# num = 100
# # 2568417465808
# print(id(num))
# myfun(num)
# # 100不是101  2568417465808
# print(num, id(num))


def myfun(num):
    print("函数内：")
    print(id(num))
    # 可变类型修改了原件
    num.append(666)
    print(id(num))

# 2555834400384所有的内存地址一致
num = [1, 2, 3]
print(id(num))
myfun(num)
print(num)

