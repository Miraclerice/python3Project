# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 9:30:54


class Person(object):
    pass


print(Person.__bases__)

'''
经典类
    没有继承(object)
新式类
    继承(object)
Python2.x版本定义一个类时, 默认不继承(object)
Python3.x版本定义一个类时, 默认继承(object)
'''
