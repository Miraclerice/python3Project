# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 14:07:50

# 多继承
# class Father:
#     pass
#
# class Mother:
#     pass
#
# class Dog(Father, Mother):
#     pass
#
#
# dog = Dog()
# print(dog.__class__)
# print(Dog.__class__)
# print(type.__class__)
# print(object.__class__)
#
# print("----------------------")
# print(Dog.__bases__)
# print(Mother.__bases__)
#
# print(int.__bases__)
# print(float.__bases__)
# print(object.__bases__)


# ------------------继承到的资源-----------------
# class Animal:
#     has_nucleus = "has_nucleus"
#     _smell = "_smell"
#     __meat = "__meat"
#
#     def __init__(self):
#         print("init, Animal")
#
#     def eat(self):
#         print("eat")
#
#     def _run(self):
#         print("_run")
#
#     def __say(self):
#         print("__say")
#
#
# class Dog(Animal):
#     def test(self):
#         print(id(Animal.has_nucleus))
#         print(self.has_nucleus)
#         print(self._smell)
#         # print(self.__meat)
#         self.eat()
#         self._run()
#         # self.__init__()
#         # self.__say()
#
#
# # print(Animal.__dict__)
# dog = Dog()
# # Animal.has_nucleus = "T"
# # 同一资源
# # print(id(Animal.has_nucleus))
# dog.has_nucleus = 10
# print(Animal.has_nucleus)
# dog.test()


# ------------------针对于几种标准原则的方案演化-----------------

import inspect


# class C(object):
#     name = "c"
#     pass
#
#
# class B(C):
#     name = "b"
#     pass
#
#
# class A(B):
#     name = "a"
#     pass
#
# print(A.name)
# print(inspect.getmro(A))


# class E(object):
#     name = "e"
#     pass
#
#
# class D(object):
#     name = "d"
#     pass
#
# class C(E):
#     name = "c"
#     pass
#
#
# class B(D):
#     name = "b"
#     pass
#
#
# class A(B):
#     # name = "a"
#     pass
#
# print(A.name)
# print(inspect.getmro(A))

# -----------------c3算法 Mro原则-----------------
# class D(object):
#     name = "d"
#     pass
#
#
# class C(D):
#     name = "c"
#     pass
#
#
# class B(D):
#     name = "b"
#     pass
#
#
# class A(B, C):
#     # name = "a"
#     pass
#
#
# # print(A.name)
# # 查看资源顺序三种方式
# print(inspect.getmro(A))
# print(A.mro())
# print(A.__mro__)


# ------------------------------菱形继承资源覆盖：属性覆盖，方法重写----------------------------
# class D(object):
#     name = "d"
#
#     def run(self):
#         print("ddd")
#
#
# class C(D):
#     name = "c"
#
#     def run(self):
#         print("ccc")
#
#
# class B(D):
#     name = "b"
#
#     def run(self):
#         print("bbb", self)
#
#     @classmethod
#     def run2(cls):
#         print("ddd", cls)
#
#
# class A(B, C):
#     # name = "a"
#     # def run(self):
#     #     print("aaa")
#     pass
#
#
# print(A.name)
# a = A()
# # 谁调用，就是谁的实例，或类
# a.run()
# A.run2()


# ------------------------------菱形继承资源累加----------------------------

# class Animal(object):
#     age = 55
#
#     def __init__(self):
#         self.sex = "female"
#
#     @classmethod
#     def run(cls):
#         print("run")
#
#     @classmethod
#     def say(cls):
#         print("say")
#
#
# class Dog(Animal):
#     friend = "cat"
#
#     def __init__(self):
#         # Animal.__init__(self)
#
#         self.name = "Dog"
#
#     @classmethod
#     def run1(cls):
#         print("runDog")
#
#     @classmethod
#     def say1(cls):
#         print("sayDog")
#
#
# dog = Dog()
# print(dog.age)
# print(dog.sex)
# print(dog.friend)
# Dog.run()
# Dog.say()
#
# Dog.run1()
# Dog.say1()
# print(dog.__dict__)


# ------------------------------菱形继承资源累加用类多次调用init方法出现问题----------------------------
# class D(object):
#     def __init__(self):
#         print("d")
#
#
# class C(D):
#     def __init__(self):
#         D.__init__(self)
#         print("c")
#
# class B(D):
#     def __init__(self):
#         D.__init__(self)
#         print("b")
#
#
# class A(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("a")
#
#
# a_obj = A()
# d
# b
# d
# c
# a


# ------------------------------super使用----------------------------

# class Animal(object):
#     age = 55
#
#     def __init__(self):
#         self.sex = "female"
#
#     @classmethod
#     def run(cls):
#         print(cls)
#         print("run")
#
#     @classmethod
#     def say(cls):
#         print("say")
#
#
# class Dog(Animal):
#     friend = "cat"
#
#     def __init__(self):
#         # Animal.__init__(self)
#         # super(Dog, self).__init__()
#         super().__init__()
#         self.name = "Dog"
#
#     @classmethod
#     def run1(cls):
#         # super(Dog, cls).run()
#         super(Dog, Dog).run()
#         # super().run()
#         print("runDog")
#
#     @classmethod
#     def say1(cls):
#         super(cls, cls).say()
#         print("sayDog")


# dog = Dog()
# print(dog.age)
# print(dog.sex)
# print(dog.friend)
# # Dog.run()
# Dog.say()

# Dog.run1()
# Dog.say1()
# print(dog.__dict__)

# ------------------------------菱形继承super使用----------------------------

# class D(object):
#     def __init__(self):
#         print("d")
#
#
# class C(D):
#     def __init__(self):
#         super(C, self).__init__()
#         print("c")
#
# class B(D):
#     def __init__(self):
#         super(B, self).__init__()
#         print("b")
#
#
# class A(B, C):
#     def __init__(self):
#         # super(A, self).__init__()
#         super().__init__()
#         print("a")
#
#
# a_obj = A()
# d
# c
# b
# a


# ------------------------------菱形继承super使用注意事项----------------------------

class D(object):
    def __init__(self):
        print("d")


class C(D):
    def __init__(self):
        print("c1")
        super(C, self).__init__()
        print("c")


class B(D):
    def __init__(self):
        print("b1")
        # self.__class__一直都是A,所以一直死循环，不建议这样写
        # super(self.__class__, self).__init__()
        super(B, self).__init__()
        print("b")


class A(B, C):
    def __init__(self):
        print("a1")
        # super(A, self).__init__()
        # super().__init__()
        B.__init__(self)
        C.__init__(self)  # d c b d c a
        print("a")


a_obj = A()
print(A.mro())
# b = B()
