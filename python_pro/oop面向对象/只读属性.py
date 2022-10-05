# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 0:33:37
from typing import Type


# class Person:
#
#     def __init__(self):
#         self.__age = 18
#
#     @property
#     def age(self):
#         return self.__age


# p = Person()
# print(p.__age)
# p.__age = 25
# print(p.__dict__)
# print(p.getAge())
# print(p.age)
# 不能设置属性
# p.age = 666

# 只读属性的方式二
class Person:
    # 当我们使用 "实例.属性 = 值" 这种格式给一个实例增加或修改属性的时候, 都会调用系统内置的这个方法
    # 在这个方法的内部, 才会真正的把属性以及对应的值给存储到 __dict__当中
    def __setattr__(self, key, value):
        print(key, value)
        if key == "age" and key in self.__dict__.keys():
            print("只读属性，不能设置属性")
        else:
            # self.key = value 死循环
            self.__dict__[key] = value

p = Person()
p.age = 15
print(p.age)
# p.name = "zz"

p.age = 66
print(p.age)
print(p.__dict__)

'''
只读属性
概念
    一个属性(一般指实例属性), 只能读取, 不能写入
应用场景
    有些属性, 只限在内部根据不同场景进行修改, 而对外界来说, 不能修改, 只能读取
    比如
        电脑类的网速属性, 网络状态属性
方式1
    方案
        全部隐藏
            私有化
                既不能读
                也不能写
        部分公开
            公开读的操作(设置方法返回私有属性)
    具体实现
        私有化
            通过"属性前置双下划线"实现
        部分公开
            通过公开的方法
            优化(加装饰器@property)
                property
                    作用
                        将一些"属性的操作方法"关联到某一个属性中
                    概念补充(使用__bases__属性查看继承的基类)
                        经典类
                            没有继承(object)
                        新式类
                            继承(object)
                        Python2.x版本定义一个类时, 默认不继承(object)
                        Python3.x版本定义一个类时, 默认继承(object)
                        建议使用
                            新式类
                    property
                        在经典类中
                            只能管理一个属性的读取操作
                        在新式类中
                            可以管理一个属性的删改查操作
方式2
    方案
        借助系统内置的方法进行拦截
    具体实现
        __setattr__方法
            当我们使用 "实例.属性 = 值" 这种格式给一个实例增加或修改属性的时候, 都会调用系统内置的这个方法
            在这个方法的内部, 才会真正的把属性以及对应的值给存储到 __dict__当中
        解决方案
            在这个方法中, 进行拦截
'''
