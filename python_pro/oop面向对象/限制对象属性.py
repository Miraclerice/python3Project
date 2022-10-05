# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 19:24:54

class Person:
    __slots__ = ["age", "name", "sex"]
    pass


p = Person()
p.age = 12
p.sex = "男"
print(p.__dict__)

'''
通过设置__slots__属性(在类的内部设置)
    列表中的元素，即为通过这个类创建出的对象可以添加的对象属性
    如果这个类实例出的对象，添加了非列表之内的属性，则会报错
'''