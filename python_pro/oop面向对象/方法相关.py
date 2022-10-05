# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 19:32:03

def eat():
    print("xxx")


# eat()


class Person:
    def example_method(self):
        print("这是一个实例方法", self)

    @classmethod
    def class_method(cls):
        print("这是一个类方法", cls)

    @staticmethod
    def static_method():
        print("这是一个静态方法")


p = Person()

# print(p)
# p.example_method()
# print(Person)
# Person.example_method(p)
# Person.class_method()
# Person.static_method()

print(p.__dict__)
print(Person.__dict__)

'''
 方法与普通函数异同：
    都封装了一系列行为动作
    都可以被调用的之后，执行一系列行为动作
    最主要的区别就是：调用方式，方法需要对象调
    
方法的划分：
    * 实例方法
        默认第一个参数需要接收到一个实例
    * 类方法(加@classmethod注解)
        默认第一个参数需要接收到一个类
    * 静态方法(加@staticmethod注解)
        第一个参数什么都不默认接收
    * 注意:
       1.划分的依据是：方法的第一个参数必须要接收的数据类型
       2.不管是哪一种类型的方法，都是存储在类当中；没有在实例当中的
       3.不同类型方法的调用方式不同
'''
