# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 21:10:15

# ----------------引用计数器------------------
# import sys
#
#
# class Person:
#     pass
#
#
# pack1 = Person()
# # 2-1
# print(sys.getrefcount(pack1))
#
# p2 = pack1
# # 3-1
# print(sys.getrefcount(pack1))
#
# del p2
# # 2-1
# print(sys.getrefcount(pack1))
#
# del pack1
# 报错
# print(sys.getrefcount(pack1))

# ----------------引用计数器 +1 -1------------------

# import sys
#
#
# class Person:
#     pass
#
#
# p = Person()
#
# print(sys.getrefcount(p))
#
# # def log(obj):
# #     print(sys.getrefcount(obj))
# #
# # log(p)
#
# l = [p]
# del l
#
#
# print(sys.getrefcount(p))


# ----------------利用计数器机制-循环有引用问题------------------
# 内存管理机制：引用计数器机制 + 垃圾回收机制
#   如果一个对象被引用 + 1    该对象被删除，引用 - 1    0：自动释放
# objgraph.count() 查看垃圾回收器跟踪的个数

import objgraph


class Cat:
    pass


class Dog:
    pass


cat = Cat()
dog = Dog()
print(objgraph.count("Cat"))
print(objgraph.count("Dog"))

cat.master = dog
dog.friend = cat

# 删除cat 和 dog 后对象 是否释放
del cat
del dog

print(objgraph.count("Cat"))
print(objgraph.count("Dog"))
