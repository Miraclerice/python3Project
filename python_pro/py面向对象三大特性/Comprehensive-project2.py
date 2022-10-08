# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 20:32:15

# 定义三个类：学生，组长，教师
# 学生：
# 	姓名， 年龄， 学号
# 	吃饭， 睡觉， 学习
# 组长：
# 	姓名， 年龄， 学号， 职务
# 	吃饭， 睡觉， 学习， 管理
# 教师
# 	姓名， 年龄， 职务
# 	吃饭， 睡觉， 教学， 管理
import abc


class Person(object, metaclass=abc.ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self}在吃饭")

    def sleep(self):
        print(f"{self}在睡觉")

    @abc.abstractmethod
    def __str__(self):
        pass


class Manager:
    # def __init__(self, position):
    #     pass

    def manage(self):
        print(f"{self}在管理")


class Student(Person):
    def __init__(self, name, student_id, age=1):
        super(Student, self).__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self}在学习")

    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}"


class Leader(Student, Manager):
    def __init__(self, name, student_id, position, age=1):
        super(Leader, self).__init__(name, student_id, age)
        self.position = position

    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.position} 职位: {self.position}"


class Teacher(Person, Manager):
    def __init__(self, name, position, age=1):
        super(Teacher, self).__init__(name, age)
        self.position = position

    def teach(self):
        print(f"{self}在教学")

    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 职位: {self.position}"


teacher = Teacher("张三", "主任", 32)
# leader = Leader("李四", 123456, "会长", 12)
# student = Student("王五", 123456,  12)
# student.study()
# leader.study()
teacher.teach()
# leader.manage()
