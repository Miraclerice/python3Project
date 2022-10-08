# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 20:27:15

# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print("创建了一个实例，但是被我拦截了")
#
#     def __init__(self):
#         self.age = "12"
#
#     def __del__(self):
#         print("实例对象释放了")
#     pass


# person = Person()
# print(person)
# print(person.age)


# 案例
class Person:
    __personCount = 0

    def __init__(self):
        print("计数 + 1")
        Person.__personCount += 1

    def __del__(self):
        print("计数 - 1")
        self.__class__.__personCount -= 1

    @classmethod
    def log(cls):
        print(f"当前人的个数{cls.__personCount}个")


# Person.__personCount = 100
person = Person()
person1 = Person()
Person.log()
del person
Person.log()


'''
__new__方法
    当我们创建一个对象是, 用于给这个对象分配内存的方法
    通过拦截这个方法, 可以修改对象的创建过程
    比如:单例设计模式
__init__方法
    每个对象实例化的时候，都会自动执行这个方法
    可以在这个方法里面，初始化一些实例属性
__del__方法
    当对象被释放的时候调用这个方法
    可用于在这个方法中清理资源
'''