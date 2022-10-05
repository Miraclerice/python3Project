# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 20:58:23

# l = [1, 15, 6]
# l.sort()
# print(sorted(l))
# print(list.sort(l))
# print(l)
class Person:
    @staticmethod
    def static_method():
        print("这是一个静态方法")


Person.static_method()
person = Person()
person.static_method()
func = Person.static_method
func()
'''
class 类名:
    @staticmethod
    def 方法名():
        方法体

类调用：不用传递个参数
实例调用：不用传递参数
看场景使用什么调用方法
'''
