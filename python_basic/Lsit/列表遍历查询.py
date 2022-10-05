# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 10:47:21

from collections.abc import Iterable
from collections.abc import Iterator

# 1) 根据元素进行遍历
# for item in list:
# values = ['a', 'b', 'c', 'd']
#
# for v in values:
#     currentIndex = 0
#     print(v)
#     print(values.index(v, currentIndex))
#     currentIndex += 1

# 2) 根据索引进行遍历
# for index in range(len(list)):
# values = ['a', 'b', 'c', 'd', 'e']
# for index in range(len(values)):
#     print(index, values[index])


# 3) 根据枚举对象进行遍历(了解)

# values = ['a', 'b', 'c', 'd', 'e']
# 1.根据列表创建枚举对象
# 语法：enumerate(list, [start=0])
# print(list(enumerate(values)))
# 2.遍历枚举对象，可以直接遍历
# for index, value in enumerate(values):
# for tupleValue in enumerate(values):
# print(tupleValue)
# print(tupleValue[0])
# print(tupleValue[1])
# index, value = tupleValue
# print(index)
# print(value)

# 4) 根据迭代器进行遍历(了解)
# l = [1, 2, 3, 5, 6]
# 创建迭代器对象
# it = iter(l)
# 内部自动调整指针，指向下一个索引
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# 迭代完成，继续迭代会报错StopIteration
# print(next(it))
# for v in it:
#     print(v)
# print("===========")
# 不能多次迭代，只能重新创建迭代器对象
# for v in it:
#     print(v)


# 迭代器
# nums = (1, 2)
# 判断是否是可迭代对象方式一
# for num in nums:
#     print(num)
# 判断是否是可迭代对象方式二
# print(isinstance(nums, Iterable))
#
# print(isinstance(nums, Iterator))
# next(nums)

# i = iter(nums)
# print(i)
# print(isinstance(i, Iterable))

# val = [1, 2, 45, 56]
# in 判断元素是否在列表中（对其他集合和字符串通用）
# not in 判断元素是否在列表中（对其他集合和字符串通用）
# print(1 in val)
# print(1 not in val)
'''
cmp(val1,val2)
内建函数
如果比较字符串，列表等集合,从左往右逐个比较
val1 > val2  1
val1 = val2  0
val1 < val2  -1
python3.x不支持

python3使用比较运算符比较
'''
# print([1, 2] > [1, 3])

# 排序方式一
# s = "happynewYear"
# s = [99, 2, 5, 6, 8, 9]
# # 升序,得到一个列表
# res = sorted(s)
# print(res)
# print(s)
# # 降序
# res1 = sorted(s, reverse=True)
# print(res1)
# s1 = [("dd1", 18), ("dd5", 16), ("dd2", 28), ("dd1", 15)]
# # 第一个值的比较排序
# print(sorted(s1))
# def getKey(x):
#     return x[1]
# # 第二个值来排序
# print(sorted(s1,key=getKey, reverse=True))

# 排序方式二:更改对象本身，返回值为None
# val = [11, 2, 45, 56]
# print(val.sort(), val)
# s = [("dd1", 18), ("dd5", 16), ("dd2", 28), ("dd1", 15)]
# print(s.sort())
# def getKey(x):
#     return x[1]
# # 第二个元素降序排序
# print(s.sort(key=getKey, reverse=True), s)

# 乱序和反转
'''
乱序
import random
random.shuffle(list) 
返回值 ：None
'''
import random
l = [1, 5, 98, 6, 2]
res = random.shuffle(l)
print(res, l)

'''
反转
list.reverse() 
返回值 ：None
'''
l = [1, 5, 98, 6, 2]
res = l.reverse()
print(res, l)
# 切片反转,返回值反转，不会改变本身
res1 = l[::-1]
print(res1, l)
