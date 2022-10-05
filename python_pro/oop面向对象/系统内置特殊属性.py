# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 11:03:29

class Person:
    """
    这是一个人的类
    """
    age = 10
    sex = "男"

    def __init__(self):
        self.name = "zz"

    def run(self):
        print("run")


# 内置特殊属性
# 	类属性
# 		__dict__ : 类的属性
# 		__bases__ : 类的所有父类构成元组
# 		__doc__ :类的文档字符串
# 		__name__: 类名
# 		__module__: 类定义所在的模块
# 	实例属性
# 		__dict__ : 实例的属性
# 		__class__: 实例对应的类

print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
# help(Person)
print(Person.__name__)
print(Person.__module__)
person = Person()
print(person.__dict__)
print(person.__class__)

