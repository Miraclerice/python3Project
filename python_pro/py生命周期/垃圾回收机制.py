# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 22:26:14

import gc

# ----------垃圾回收机制   分代回收机制------------


# print(gc.get_threshold())
# gc.set_threshold(500, 20, 20)
# print(gc.get_threshold())

# ----------垃圾回收机制   触发时机------------
# print(gc.isenabled())
#
# gc.disable()
# print(gc.isenabled())
#
# gc.enable()
# print(gc.isenabled())
# print(gc.get_threshold())
# gc.set_threshold(1000, 20, 10)
# print(gc.get_threshold())


# ----------------利用垃圾回收机制-循环有引用问题------------------
# 内存管理机制：引用计数器机制 + 垃圾回收机制
#   如果一个对象被引用 + 1    该对象被删除，引用 - 1    0：自动释放
# objgraph.count() 查看垃圾回收器跟踪的个数

import objgraph

# 触发垃圾回收机制与垃圾回收机制是否开启无关
gc.disable()


class Cat:
    def __del__(self):
        print("cat对象被释放了")
    pass


class Dog:
    def __del__(self):
        print("dog对象被释放了")
    pass


cat = Cat()
dog = Dog()
print(objgraph.count("Cat"))
print(objgraph.count("Dog"))

# 让两个对象相互引用，造成循环引用
cat.master = dog
dog.friend = cat

# 删除cat 和 dog 后对象 是否释放，尝试通过删除可到达引用之后，真实对象是否能被回收
del cat
del dog

# 通过引用计数器无法回收，借助触发垃圾回收机制进行回收
gc.collect()

print(objgraph.count("Cat"))
print(objgraph.count("Dog"))
