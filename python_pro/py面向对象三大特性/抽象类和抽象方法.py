# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 20:09:11
import abc


class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass

    # 过时了
    # @abc.abstractclassmethod
    @classmethod
    @abc.abstractmethod
    def fly(cls):
        pass


class Dog(Animal):
    def say(self):
        print("汪汪汪")
    def fly(cls):
        print("no")


class Cat(Animal):
    def say(self):
        print("喵喵喵")
    def fly(cls):
        print("我只会跳")


def func(obj):
    obj.say()


cat = Cat()
dog = Dog()
cat.fly()
func(cat)
func(dog)
# Animal().say()
