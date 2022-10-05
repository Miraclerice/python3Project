# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 21:30:49

# num = 10
# print(num.__class__)
#
# str1 = "jjj"
# print(str1.__class__)
#
#
# class Person:
#     pass
#
#
# p = Person()
# print(p.__class__)
#
#
# print("-" * 100)
# print(int.__class__)
# print(str.__class__)
# print(Person.__class__)
# print(Person.__class__.__class__)
# print(type.__class__)


# 类创建方式
# class Person:
#     age = 10
#     def run(self):
#         print("run")

# num = 10
# print(type(num))

# def run(self):
#     print("dog--", self)
#
# 使用type创建类
# xxx = type("Dog", (), {"count": 0, "run": run})
# # print(xxx)
# print(xxx.__dict__)
# dog = xxx()
# print(dog)
# dog.run()


# 类的创建流程
# __metaclass__ = "xxx"

class Animal:
    pass


class Person(Animal):
    # __metaclass__ = xxx
    pass



'''
类创建流程：
    1. 检测类中是否有明确 __metaclass__属性，有, 则通过指定元类来创建这个类对象
    2. 检测父类中是否存在__metaclass__属性，有, 则通过指定元类来创建这个类对象
    3. 检测模块中是否存在__metaclass__属性，有, 则通过指定元类来创建这个类对象
    4. 通过内置的type这个元类,来创建这个类对象
    4. 通过内置的type这个元类,来创建这个类对象
场景：1)   拦截类的创建  2)   修改类   3)   返回修改之后的类
后面补充
'''