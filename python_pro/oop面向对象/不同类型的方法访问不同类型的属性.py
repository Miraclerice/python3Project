# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 21:13:01

class Person:
    # 类属性
    age = 10

    def instance_method(self):
        print(self)
        # 实例方法可以访问实例属性和类属性
        print(self.age)
        print(self.num)

    @classmethod
    def class_method(cls):
        print(cls)
        print(cls.age)
        # (没有传实例对象参数前提)
        # 类方法不能访问类属性
        # print(cls.num)

    @staticmethod
    def static_method():
        print(Person.age)
        # (没有传实例对象参数前提)
        # print(p.num)


p = Person()
# 访问类属性
# print(Person.age)
# print(p.age)
# 实例属性
p.num = 666
# print(p.num)
# print(Person.num)

p.instance_method()
p.class_method()
p.static_method(p)

