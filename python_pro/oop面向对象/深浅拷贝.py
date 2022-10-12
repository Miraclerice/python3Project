# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022-10-11 14:09:30
# class Person:
#     def __init__(self, uid, name, age):
#         self.uid = uid
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"uid: {self.uid},name: {self.name},age: {self.age}"
#
#
# class Teacher(Person):
#     def __init__(self, uid, name, age, tid=1):
#         super(Teacher, self).__init__(uid, name, age)
#         self.tid = tid
#
#     def __getattr__(self, item):
#         return item.
#
#     def __str__(self):
#         return super(Teacher, self).__str__() + f", tid = {self.tid}"
#
#
# class Student(Person):
#     def __init__(self, uid, name, age, sid=1):
#         super(Student, self).__init__(uid, name, age)
#         self.sid = sid
#
#     def __str__(self):
#         return super(Student, self).__str__() + f", sid = {self.sid}"
#
#
# print("-------------------student------------------------")
# student = Student(1, "zhangsan", 12)
# print(student)
# # 获取属性值
# print(student.__getattribute__("name"))
#
# print("-------------------teacher------------------------")
# teacher = Teacher(2, "wanglaoji", 45, 12)
# print(teacher)
# print(teacher.__getattr__("name"))

# # 注解
# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
#
#
# print(f("ll"))


# -----------------------深拷贝-----------------------------------
# class Cpu:
#     def __init__(self, value):
#         self.cpu = value
#
#
# class Disk:
#     def __init__(self, value):
#         self.disk = value
#
#
# class Computer:
#     def __init__(self, cpu, disk):
#         self.cpu = cpu
#         self.disk = disk


# print("--------------变量赋值---------------")
# num1 = 12
# num2 = num1
# 同时指向一块内存空间
# print(id(num1), id(num2))


# print("--------------实例变量赋值---------------")
# cpu = Cpu("英特尔")
# disk = Disk("联想")
# computer = Computer(cpu, disk)
# 你要是认为是computer2没有实例化才会一模一样，你也可以实例化，发现就是一样的
# computer2 = computer
# print(computer, computer.disk, computer.cpu)
# print(computer2, computer2.disk, computer2.cpu)

# print("--------------实例浅拷贝---------------")
# import copy
# cpu = Cpu("英特尔")
# disk = Disk("联想")
# computer = Computer(cpu, disk)
# computer2 = copy.copy(computer)
# # 只有子对象相同，指明子对象没有拷贝，对象本身拷贝了
# print(computer, computer.disk, computer.cpu)
# print(computer2, computer2.disk, computer2.cpu)

# print("--------------实例深拷贝---------------")
# import copy
# cpu = Cpu("英特尔")
# disk = Disk("联想")
# computer = Computer(cpu, disk)
# computer2 = copy.deepcopy(computer)
# # 对象本身与他的子对象都拷贝了
# print(computer, computer.disk, computer.cpu)
# print(computer2, computer2.disk, computer2.cpu)
