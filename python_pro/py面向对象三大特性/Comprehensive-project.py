# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 20:32:15

# 定义三个类, 小狗, 小猫, 人
# 小狗: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 看家(格式: 名字是xx, 年龄xx岁的小狗在xx)
# 小猫: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 捉老鼠(格式: 名字是xx, 年龄xx岁的小猫在xx)
# 人:   姓名, 年龄(默认1岁), 宠物;  吃饭, 玩, 睡觉(格式: 名字是xx, 年龄xx岁的小猫在xx)
#                           养宠物(让所有的宠物吃饭, 玩, 睡觉),
#                           让宠物工作(让所有的宠物根据自己的职责开始工作)


# class Dog:
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self}吃饭")
#
#     def play(self):
#         print(f"{self}玩")
#
#     def sleep(self):
#         print(f"{self}睡觉")
#
#     # def see_home(self):
#     def work(self):
#         print(f"{self}看家")
#
#     def __str__(self):
#         return f"名字是{self.name}, 年龄{self.age}岁的小狗在"
#
#
# class Cat:
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self}吃饭")
#
#     def play(self):
#         print(f"{self}玩")
#
#     def sleep(self):
#         print(f"{self}睡觉")
#
#     # def catch_mouse(self):
#     def work(self):
#         print(f"{self}捉老鼠")
#
#     def __str__(self):
#         return f"名字是{self.name}, 年龄{self.age}岁的小猫在"
#
#
# class Person:
#     def __init__(self, name, pets, age=1):
#         self.name = name
#         self.age = age
#         self.pets = pets
#
#     def eat(self):
#         print(f"{self}吃饭")
#
#     def play(self):
#         print(f"{self}玩")
#
#     def sleep(self):
#         print(f"{self}睡觉")
#
#     def keep_pets(self):
#         for pet in self.pets:
#             pet.eat()
#             pet.play()
#             pet.sleep()
#
#     def make_pets_work(self):
#         for pet in self.pets:
#             pet.work()
#             # if isinstance(pet, Dog):
#             #     pet.see_home()
#             # if isinstance(pet, Cat):
#             #     pet.catch_mouse()
#
#     def __str__(self):
#         return f"名字是{self.name}, 年龄{self.age}岁的小孩在"
#
#
# dog = Dog("旺财", 12)
# # dog.eat()
# # dog.sleep()
# cat = Cat("小花")
# person = Person("xie", [dog, cat], 15)
# # person.keep_pets()
# person.make_pets_work()


# ----------------------------------------优化----------------------------------------
class Animal(object):
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self}吃饭")

    def play(self):
        print(f"{self}玩")

    def sleep(self):
        print(f"{self}睡觉")


class Dog(Animal):
    def work(self):
        self.__see_home()

    def __see_home(self):
        print(f"{self}在看家")

    def __str__(self):
        return f"名字是{self.name}, 年龄{self.age}岁的小狗在"


class Cat(Animal):
    def work(self):
        self.__catch_mouse()

    def __catch_mouse(self):
        print(f"{self}捉老鼠")

    def __str__(self):
        return f"名字是{self.name}, 年龄{self.age}岁的小猫"


class Person(Animal):
    def __init__(self, name, pets, age=1):
        super(Person, self).__init__(name, age)
        self.pets = pets

    def keep_pets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()

    def __str__(self):
        return f"名字是{self.name}, 年龄{self.age}岁的天才"


dog = Dog("旺财", 12)
# dog.eat()
# dog.sleep()
cat = Cat("小花")
person = Person("xie", [dog, cat], 15)
print(person)
person.keep_pets()
person.make_pets_work()
