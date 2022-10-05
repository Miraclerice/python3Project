# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 23:13:57

s1 = {1, 2, 3, 5, 6, 9}
s2 = {2, 4, 3, 9, 8}
'''
交集
intersection(iterable) 
    字符串(只判断非数字）
    元组
    集合
    列表
    字典(只判断key)
    ...
    
逻辑与'&' 集合本身不会改变
intersection_update(iterable)
    交集计算完后会赋值给原集合，所以只适用于可变集合
'''
# res = s1.intersection(s2)
# set
# print(res, type(res))
# s3 = {1, 2, 3, 5, 6, 9}
# s4 = frozenset([2, 4, 3, 9, 8])
# frozenset
# res1 = s4.intersection(s3)
# print(res1, type(res1))

# res2 = s1.intersection_update(s2)
# res2:None s1:{9, 2, 3} s2:{2, 3, 4, 8, 9}
# print(res2, type(res2), s1, s2)

# 集合本身不会改变
# res3 = s1 & s2
# print(res3, type(res3), s1, s2)

# # set() 因为不会判断数字
# print(s1.intersection("123"))
# s5 = {"1", "2", "5"}
# # 只能判定字符串
# print(s5.intersection("123"))
# print(s5.intersection(["1", "2", "6"]))
# # 不能存在不可哈希的值["1", "5"]
# print(s5.intersection(["1", "2", ["1", "5"]]))
# print(s5.intersection({"1": "vv", "2": "jj", "6": "55"}))

'''
并集
union()
    返回并集
逻辑或'|'
    返回并集
update()
    更新并集,原左侧集合更新为并集
'''
# s3 = {1, 2, 3}
# s3 = frozenset([1, 2, 3])
# s4 = {4, 2, 5}

# res1 = s3.union(s4)
# res1 = s3 | s4
# None, s3:{1, 2, 3, 4, 5}
# res1 = s3.update(s4)
# print(res1, type(res1), s3, s4)

'''
差集
difference()
    返回差集
算术运算符'-' 
    返回并集
update()
    更新并集,原左侧集合更新为并集
'''
# s3 = {1, 2, 3}
# s3 = frozenset([1, 2, 3])
# s4 = {4, 2, 5}

# res1 = s3.difference(s4)
# res1 = s3 - s4
# None, s3:{1, 3}
# res1 = s3.difference_update(s4)
# print(res1, type(res1), s3, s4)


'''
判定
两个集合不相交：isdisjoint()
一个集合包含另一个集合：issuperset()
一个集合包含于另一个集合：issubset()
'''
set1 = {1, 2, 3}
set2 = {1, 2}
# False
print(set1.isdisjoint(set2))
# True
print(set1.issuperset(set2))
# False
print(set1.issubset(set2))
print(set1.issubset(set1))
