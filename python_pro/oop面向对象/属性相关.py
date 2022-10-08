# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 16:27:34


# class Person:
#     pass


# 创建对象
# person = Person()
# person.age = 18
# person.height = 190
# person.age = 23
# print(person.age)
# # 获取对象所有属性
# print(person.__dict__)
# # print(person.sex)
# person.letter = ["aa", "bb"]
# print(person.letter, id(person.letter))
# # 修改操作
# person.letter = [1, 2]
# print(person.letter, id(person.letter))
# # 访问操作，内存空间位置不变
# person.letter.append(3)
# print(person.letter, id(person.letter))

# person.age = 10
# del person.age
# print(person.age)

# class Person:
#     pass


# pack1 = Person()
# p2 = Person()
#
# p2.age = 18
# print(pack1.age)

# class Person:
#     num = 666
#     age = 16
#     count = 12


# class Monkey:
#     sex = "男"


# Person.age = 10


# print(Person.age)
# print(Person.num)
# print(Person.__dict__)
# p = Person()
# print(p.__class__)
# p.__class__ = Monkey
# print(p.__class__)
# p.sex = "女"
# print(p.sex)
# print(p.age)
# print(p.count)
# print(p.num)
# print(p.__dict__)


# class Person:
#     num = 666
#     age = 16
#     count = 12


# del Person.num
# print(Person.num)
# p = Person()
# print(p.num)
# 不能操作
# del p.age
# print(p.age)
# print(Person.age)
# Person.count = 22
# print(Person.count)
#
# p = Person()
# p.num = 10
# print(p.num)
# print(Person.num)


class Person:
    name = "xie"
    age = 18


# attribute '__dict__' of 'type' objects is not writable
# Person.__dict__ = {"sex": "男"}
# 'mappingproxy' object does not support item assignment
# Person.__dict__["age"] = 20
# print(Person.__dict__)


p = Person()
p1 = Person()
Person.age = 666
print(p.age)
print(p1.age)


# p.age = 10
# p.height = 100
# print(p.__dict__)

# p.__dict__ = {'age': 10, 'height': 100}
# p.__dict__["age"] = 15
# print(p.age)
# print(p.__dict__)
'''
对象属性(java没有对象属性概念，python有)
    * 使对象具有一些属性（增）
        1.直接通过对象，动态添加，对象.属性 = 值
        2.通过类的初始化方法(构造方法） __init__方法
    * 访问对象的属性（查）
        对象.属性
        查看对象属性是否添加成功:打印对象.属性,或者获取所有该对象属性，对象.__dict__
    * 修改对象的属性（改）
        对象.属性 = 新值
        修改操作，属性会指向新的空间(不可变类型),可变类型的值会修改值，指向的内存地址不变
    * 删除对象的属性（删）
        del 对象.属性
    * 对象名访问属性，其实是访问对象的__dict__属性指向地址的属性值，可以通过（对象.__dict__ = 字典）给对象设置属性,说明了__dict__属性可以修改
        
    可以通过对象.__class__ = 类名 来修改所属类
    
类属性(类本身、及根据该类创建的对象都可以共享)
    * 使类具有一些属性（增）
        1.直接通过类名，动态添加，类名.属性 = 值
        2.在类的代码块直接写属性名 = 值
    * 访问类的属性（查）
        类名.属性
        查看类属性是否添加成功:打印 类名.属性,或者获取所有该类属性，类名.__dict__
        * python对象属性查找机制，python对象会优先查找对象自身属性，找不到才根据__class__去对象对应的类属性查找
    * 修改类的属性（改）
        类名.属性 = 新值
        修改操作，属性会指向新的空间(不可变类型),可变类型的值会修改值，指向的内存地址不变
        * 属于该类创建的对象修改类属性，成为对象自己的属性，属于新增操作，但不会修改类属性
    * 删除类的属性（删）
        del 类名.属性
        不能使用del 对象.属性,会报错，即不能通过对象删除类属性
'''
