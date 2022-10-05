# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 11:22:01

# ----------------信息格式化操作:__str__方法-------------------------

# class Person:
#     # 类的构造方法，self相当于java的this关键字
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
#
#     # 相当于java自己重写的toString()方法
#     def __str__(self):
#         # return "这个人的身高是%s, 年龄是%s" % (self.height, self.weight)
#         # return "这个人的身高是%(height)s, 年龄是%(weight)s" % ({"height": self.height, "weight": self.weight})
#         # return "这个人的身高是{0}, 年龄是{1}".format(self.height, self.weight)
#         return f"这个人的身高是{self.height}, 年龄是{self.weight}"
#
#
# p1 = Person(40, 152)
# print(p1.height)
# print(p1.weight)
# print(p1)
#
#
# p2 = Person(70, 190)
# print(p2.height)
# print(p2.weight)
# print(p2)
#
# s = str(p1)
# print(s, type(s))


# ----------------信息格式化操作:__repr__方法-------------------------

# class Person:
#     # 类的构造方法，self相当于java的this关键字
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
#
#     # 相当于java自己重写的toString()方法
#     def __str__(self):
#         # return "这个人的身高是%s, 年龄是%s" % (self.height, self.weight)
#         # return "这个人的身高是%(height)s, 年龄是%(weight)s" % ({"height": self.height, "weight": self.weight})
#         # return "这个人的身高是{0}, 年龄是{1}".format(self.height, self.weight)
#         return f"这个人的身高是{self.height}, 年龄是{self.weight}"
#
#     def __repr__(self):
#         return "vvv"
#
# p1 = Person(40, 152)
# print(p1)
#
#
# p2 = Person(70, 190)
# print(p2)
#
# # s = str(p1)
# # print(s, type(s))
#
# print(repr(p1))


# import datetime
#
# t = datetime.datetime.now()
# print(t)
# tmp = repr(t)
# # 面向开发人员
# print(tmp)
# # 面向用户
# print(eval(tmp))


# ----------------调用操作: __call__方法-------------------------

# class Person:
#     def __call__(self, *args, **kwargs):
#         print("xxx", args, kwargs)
#
#     pass
#
#
# p = Person()
# p(12, 56, name="jj")
import collections.abc
import functools


# 关键字参数放后面
# def getColorPen(pen_color, pen_type):
#     print(f"{pen_type}的颜色是{pen_color}")
#
#
# pen = functools.partial(getColorPen, pen_type="钢笔")
# pen("红色")
# pen("绿色")
# pen("蓝色")


# class PenFactory:
#     def __init__(self, pen_type):
#         self.pen_type = pen_type
#
#     def __call__(self, pen_color):
#         print(f"{self.pen_type}的颜色是{pen_color}")
#
#
# p = PenFactory("钢笔")
# p("红色")
# p("绿色")
# p("蓝色")
# pencil = PenFactory("铅笔")
# pencil("红色")
# pencil("绿色")
# pencil("蓝色")


# ----------------索引操作-------------------------
# class Person:
#     def __init__(self):
#         self.cache = {}
#
#     def __setitem__(self, key, value):
#         # print("__setitem__", key, value)
#         self.cache[key] = value
#
#     def __getitem__(self, item):
#         # print("__getitem__", item)
#         return self.cache[item]
#
#     def __delitem__(self, key):
#         # print("__delitem__", key)
#         del self.cache[key]
#     pass
#
#
# person = Person()
# person["name"] = "zhangsan"
# print(person["name"])
# del person["name"]
# # print(person["name"])
# print(person.cache)


# ----------------索引操作-------------------------
# class Person:
#     def __init__(self):
#         self.items = [1, 2, 3, 5, 6, 8, 9]
#
#     def __setitem__(self, key, value):
#         if isinstance(key, slice):
#             self.items[key.start: key.stop: key.step] = value
#
#     def __getitem__(self, item):
#         # print("get", item)
#         if isinstance(item, slice):
#             return self.items[item.start:item.stop:item.step]
#
#     def __delitem__(self, key):
#         # print("del", key)
#         del self.items[key]
#
#
# p = Person()
# p[0:4:2] = ["l", "m"]
# print(p[0:4:2])
# del p[0:4:2]
# print(p.items)

# ----------------比较操作-------------------------
# python 2.x 可以直接使用 > < >= <= != ==比较
# python3.x需要实现六个方法才能使用，实现逻辑，但是方法不会叠加操作，不如eq方法与lt方法不会叠加为le方法
# class Person:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
#
#     # """
#     # 等于，可以由__ne__通过调换参数反推导出来，也可以自己写
#     # """
#     #
#     # def __eq__(self, other):
#     #     print("__eq__")
#     #     return self.age == other.age
#     #
#     # """
#     #    不等于，可以由__eq__通过调换参数反推导出来，也可以自己写
#     # """
#     #
#     # def __ne__(self, other):
#     #     print("__ne__")
#     #     return self.age != other.age or self.height != other.height
#     #
#     # """
#     #  大于，可以由__lt__通过调换参数反推导出来，也可以自己写
#     # """
#     #
#     # def __gt__(self, other):
#     #     print("__gt__")
#     #
#     """
#        小于，可以由__gt__通过调换参数反推导出来，也可以自己写
#     """
#
#     def __lt__(self, other):
#         print("__lt__")
#         # 当为大于号时参数调换
#         print(self.age)
#         print(other.age)
#         return self.age < other.age
#
#     # """
#     # 于等于，可以由__le__通过调换参数反推导出来，也可以自己写
#     # """
#     #
#     # def __ge__(self, other):
#     #     print("__ge__")
#     #
#     # """
#     # 大于等于，可以由__ge__通过调换参数反推导出来，也可以自己写
#     # """
#     #
#     # def __le__(self, other):
#     #     print("__le__")
#
#
# p1 = Person(10, 160)
# p2 = Person(19, 170)
# print(p1 < p2)
# print(p1 > p2)

# ----------------比较操作_补充-------------------------
# import functools
#
#
# # 加下面装饰器至少必须有六个方法的其中一个
# @functools.total_ordering
# class Person:
#     def __eq__(self, other):
#         print("eq")
#         pass
#
#     def __lt__(self, other):
#         print("lt")
#         return False
#
#
# p1 = Person()
# p2 = Person()
# print(p1 <= p2)
# # print(Person.__dict__)


# # ----------------上下文环境中的布尔值-------------------------
# class Person:
#     def __init__(self):
#         self.age = 18
#
#     def __bool__(self):
#         return self.age >= 18
#
#
# p1 = Person()
# if p1:
#     print("实例为真")

# ----------------遍历操作-------------------------
# 遍历操作方式一
# class Person:
#     def __init__(self):
#         self.res = 1
#
#     def __getitem__(self, item):
#         self.res += 1
#         if self.res >= 6:
#             raise StopIteration("停止遍历")
#         return self.res
#
#
# p = Person()
# for i in p:
#     print(i)


# 遍历操作方式二
# class Person:
#     def __init__(self):
#         self.res = 1
#
#     def __iter__(self):
#         print("iter")
#         # 返回迭代器
#         # return iter([1, 2, 3, 4, 6])
#         return self
#
#     def __next__(self):
#         self.res += 1
#         if self.res >= 6:
#             raise StopIteration("停止遍历")
#         return self.res
#
# p = Person()
# # for i in p:
# #     print(i)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# # print(next(p))


# ----------------遍历操作,恢复迭代器初始值-------------------------
class Person:
    def __init__(self):
        self.res = 1

    # 方式一
    # def __getitem__(self, item):
    #     self.res += 1
    #     if self.res >= 6:
    #         raise StopIteration("停止遍历")
    #     return self.res

    # 方式二
    def __iter__(self):
        # 每次迭代重新赋值，使得迭代器重用
        self.res = 1
        return self

    # def __next__(self):
    #     self.res += 1
    #     if self.res >= 6:
    #         raise StopIteration("停止遍历")
    #     return self.res

    def __call__(self, *args, **kwargs):
        self.res += 1
        if self.res >= 6:
            raise StopIteration("停止遍历")
        return self.res


p = Person()
# 前提是实现了__getitem__方法，才可以使用iter()
# pt = iter(p.__next__, 4)
# 实例可以被调用，实现call方法
pt = iter(p, 4)
print(pt)
print(p is pt)
for i in pt:
    print(i)

# for i in p:
#     print(i)

# 可迭代对象或迭代器肯定可以for in，但是可以for in 不一定是可迭代对象或迭代器
from collections.abc import *

# 实例成为迭代器条件：写__iter__方法与__next__方法
# 判断是不是迭代器对象
print(isinstance(p, Iterator))
# 判断是不是可迭代对象
print(isinstance(p, Iterable))
print(isinstance(pt, Iterator))
print(isinstance(pt, Iterable))

'''
内置特殊方法
    1.生命周期方法[链接过去]
    2.其他内置方法
        a.信息格式化操作
            __str__方法
                作用
                    一个对象的描述字符串, 更加方便用户阅读, 对用户更友好
                触发方式
                    print 打印一个对象时
                    str() 函数时
                格式
                    def __str__(self):
    return "描述信息"
            __repr__方法
                作用
                    一个对象的描述字符串, 更加方便机器处理, 对机器更友好(开发人员查看)
                触发方式
                    当我们在交互模式下, 直接执行某个变量, 就会输出对应信息
                    repr() 函数时
                格式
                    def __repr__(self):
    return "描述信息"
                注意
                    一般情况下, 应满足如下等式
                        obj == eval(repr(obj))
                    或者描述一个实例详细的信息(类名等等)
        b.调用操作
            __call__方法
                作用
                    使得“对象”具备当做函数，来调用的能力
                使用
                    1. 实现实例方法 __call__
                    2. 那么创建好的实例, 就可以通过函数的形式来调用
                        实例(参数)
                应用场景
                    有点类似于之前所讲的"偏函数"的应用场景
                    可以将"常变参数"和"不常变参数"进行分离
                案例
                    不同类型的笔, 画不同的图形
        c.索引操作
            作用
                可以对一个实例对象进行索引操作
            步骤
                1. 实现三个内置方法
                    设置元素的方法
                        def __setitem__(self, key, value):
                    获取元素的方法
                        def __getitem__(self, item):
                    删除元素的方法
                        def __delitem__(self, key):
                2. 可以以索引的形式操作对象
                    增/改
                        p[1] = 666
                        p["name"] = "sz"
                    查
                        p["name"]
                        p[1]
                    删
                        del p["name"]
                        del p[1]
        d.切片操作
            作用
                可以对一个实例对象进行切片操作
            步骤
                Python2.x
                    1. 实现三个内置方法
                        __setspice__
                            设置某个元素切片时调用
                        __getspice__
                            获取某个元素切片时调用
                        __delspice__
                            删除某个元素切片时调用
                    2. 可以直接按照切片的方式操作对象
                        p[1, 6, 2]
                    * 注意: 过期
                Python3.x
                    统一由"索引操作"进行管理
                        def __setitem__(self, key, value):
                        def __getitem__(self, item):
                        def __delitem__(self, key):
        e.比较操作
            作用
                可以自定义对象 "比较大小, 相等以及真假" 规则
            步骤
                实现6个方法
                    相等
                        __eq__
                    不相等
                        __ne__
                    小于
                        __lt__
                    小于或等于
                        __le__
                    大于
                        __gt__
                    大于或等于
                        __ge__
            注意
                如果对于反向操作的比较符, 只定义了其中一个方法, 但使用的是另外一种比较运算, 那么, 解释器会采用调换参数的方式进行调用该方法
                    例如
                        定义了 "小于" 操作
                            x < y
                        使用 x > y
                            会被调换参数, 调用上面的 "小于操作"
                但是, 不支持叠加操作
                    例如
                        定义了 "小于" 和 "等于" 操作
                        不能使用 x <= y
            补充
                使用装饰器, 自动生成"反向" "组合"的方法
                    步骤
                        1. 使用装饰器装饰类
                            @functools.total_ordering
                        2. 实现
                            > 或 >= 或 < 或 <= 其中一个
                            实现 ==
                上下文环境中的布尔值
                    控制类中__bool__方法，返回布尔值来控制实例真假
        f.遍历操作
            怎样让我们自己创建的对象可以使用for in 进行遍历?
                * 实现__getitem__方法
                    优先级低
                    每次for in 获取数据时, 都会调用这个方法
                * 或者实现__iter__方法
                    优先级高
                    这个方法, 必须返回一个"迭代器";即, 具备"__iter__"和"__next__"方法
                    当for in 遍历这个对象时, 会调用这个__iter__方法;返回的迭代器对象的__next__方法
            怎样让我们自己创建的对象可以使用next函数进行访问?
                实现__next__方法
            补充
                1. __iter__方法可以恢复迭代器的初始化值, 复用迭代器
                2. "可迭代" 与 "迭代器"必须实现的方法
                3. iter方法的使用
        描述器
            概念
                可以描述一个属性操作的对象
                    对象
                    属性的操作
                        增/改
                        删
                        查
                    描述
            作用
                可以代为管理一个类属性的读写删操作, 在相关方法中, 对数据进行验证处理, 过滤处理等等
                如果一个类属性被定义为描述器，那么以后对这个类属性的操作(读写删), 都将由这个描述器代理
            定义
                定义方式1
                    property
                定义方式2
                    三个方法
                        __get__
                        __set__
                        __delete__
            调用细节
                使用实例进行调用
                    最多三个方法都会被调用
                使用类进行调用
                    最多会调用get方法
                不能够顺利转换的场景
                    新式类和经典类
                        描述器仅在新式类中生效
                    方法拦截
                        一个实例属性的正常访问顺序
                            实例对象自身的__dict__字典
                            对应类对象的__dict__字典
                            如果有父类, 会再往上层的__dict__字典中检测
                            如果没找到, 又定义了__getattr__方法, 就会调用这个方法
                        而在上述的整个过程当中, 是如何将描述器的__get__方法给嵌入到查找机制当中?
                        就是通过这个方法进行实现
                            __getattribute__
                            内部实现模拟
                                如果实现了描述器方法__get__就会直接调用
                                如果没有, 则按照上面的机制去查找
            注意
                "资料描述器"和"非资料描述器"
                    如果实现了
                        _get__
                        判定为"非资料描述器"
                    如果实现了
                        __get__
                        __set__
                        判定为"资料描述器"
                描述器和实例属性同名时, 操作的优先级问题
                    资料描述器 > 实例字典 > 非资料描述器
        装饰器
            使用类当做装饰器来使用

'''
