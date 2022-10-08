# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 21:59:20

string = "kkkk"
l = [1, 2, 3]
t = (1, 2, 3)
dic = {"name": "admin", "age": 18, "height": 666}

# 可变集合
'''
s = {1, 2, 3}
print(s, type(s))

set1 = set(string)
print(set1, type(set1))

set2 = set(l)
print(set2, type(set2))

set3 = set(t)
print(set3, type(set3))

# 生成key集合
set4 = set(dic)
print(set4, type(set4))

# 集合推导式
# set5 = set(x for x in range(10) if x % 2 == 0)
set5 = {x for x in range(10) if x % 2 == 0}
print(set5, type(set5))
'''

# 不可变集合
# fs1 = frozenset("avc")
# print(fs1, type(fs1))
# fs = frozenset(x ** 2 for x in range(10) if x % 2 == 0)
# print(fs, type(fs))

# s = {}
# s = set()
# s = frozenset()
# 不能是字典，可变类型
# s = {1, 2, 2, 3, {"gg": "l"}}

# s = {1, 2, 2, 3, (1, 2)}
# 不能是列表，可变类型
# s = {1, 2, 2, 3, [1, 2]}

# s = {1, 2, 2, 3, "kk"}
# print(s, type(s))


# s = {1, 2, 3}
# print(s, type(s))
# 集合常用操作方法
# 增 返回值None
# add = s.add(4)
# print(s, type(s), add)

# 删
# s.remove(element) 返回值None 没有该元素，报错KeyError
# remove = s.remove(4)
# remove = s.remove(5)
# print(s, type(s), remove)

# s.discard(element) 返回值None 没有该元素，什么都不会发生
# discard = s.discard(5)
# print(s, type(s), discard)

#
# s.pop(element) 随机删除并返回集合中的某个元素，集合为空，报错
# pack1 = s.pop()
# print(pack1)
# s.pop()
# s.pop()
# s.pop()
# s.pop()

# s.clear() 返回值None，清空集合，集合仍存在
# clear = s.clear()
# print(s, clear)


# 查
# 无法通过索引或key进行查询
s = {1, 2, 3}
# for v in s:
#     print(v)

# 1.生成一个迭代器
# its = iter(s)
# 2.使用迭代器取访问(next()  或 for in)
# print(next(its))
# print(next(its))
# print(next(its))
# 指针为null
# print(next(its))
#
# for it in its:
#     print(it)
#
# print("==========")
# 迭代一次后，迭代器对象需要重新创建才可以遍历
# for it in its:
#     print(it)

# 不 可变集合查询
fs = frozenset([1, 2, 3])
for f in fs:
    print(f)
ifs = iter(fs)

# print(next(ifs))
# print(next(ifs))
# print(next(ifs))

for i in ifs:
    print(i)


