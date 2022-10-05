# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 20:38:36

class Person:
    @classmethod
    def eat(cls, num):
        print(cls, num)


person = Person()
person.eat(666)
Person.eat(999)

eat = Person.eat
eat(555)


class A(Person):
    pass


A.eat(777)

'''
class 类名:
    @classmethod
    def 方法名(cls):
        方法体

类调用：不用手动传递第一个参数，会自动的把调用的类本身给传递过去(一般使用类调用)
实例调用：不用手动传递第一个参数，会自动的把调用的对象对应的类给传递过去
'''