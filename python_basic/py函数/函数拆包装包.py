# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 11:13:05

# def mySum(a, b, c, d):
#     print(a + b + c + d)
#
#
# def myFun(*args):
#     print(args)
#     # 拆包
#     print(*args)
#     mySum(*args)
#     mySum(args[0], args[1], args[2], args[3])
#     # 此时只有a能接收值，且为元组，报错
#     mySum(args)
#
#
# myFun(1, 2, 3, 4)

def mySum(a, b):
    print(a + b)


def test(**kwargs):
    print(kwargs, type(kwargs))
    # 拆包操作
    # 无法打印，报错
    # print(**kwargs)
    # 同理一个字典传参，b没有接收值报错
    # mySum(kwargs)
    mySum(**kwargs)

test(a=15, b=12)

'''
参数装包：把传递进来的参数包装成一个集合
参数拆包：把集合参数再次分解成单独的个体
'''
