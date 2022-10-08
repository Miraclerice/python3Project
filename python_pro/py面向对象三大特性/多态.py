# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 19:56:32
class Animal(object):
    def say(self):
        pass


class Dog(Animal):
    def say(self):
        print("汪汪汪")


class Cat(Animal):
    def say(self):
        print("喵喵喵")


def func(obj):
    obj.say()


cat = Cat()
dog = Dog()
func(cat)
func(dog)
