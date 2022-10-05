# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 23:24:53

# 列表添加操作

'''
append
作用：往列表最后追加一个元素
语法：list.append(object)
参数：object为添加的元素
返回值：None
注意：会修改原列表
'''
# nums = [1, 2, 3, 4]
# print(nums)
# print(nums.append(5))
# print(nums)

'''
append
作用：往列表指定索引处追加一个元素
语法：list.insert(index, object)
参数：index为索引（下标），object为添加的元素
返回值：None
注意：会修改原列表
'''
# nums = [1, 2, 3, 4]
# print(nums)
# print(nums.insert(1, 5))
# print(nums)


'''
extend
作用：往列表拓展另一个可迭代序列
语法：list.extend(iterable)
参数：iterable为可迭代集合
        字符串、列表、元组、等等 
返回值：None
注意：会修改原列表，和append区别是两个集合的拼接
'''
# nums = [1, 2, 3, 4]
# nums2 = ["a", "b", "c"]
# print(nums)
# print(nums.extend(nums2))
# print(nums)

# 乘法运算
# nums = [1, 2, 3, 4]
# print(nums * 3)

# 加法运算
# nums1 = [1, 2, 3, 4]
# nums2 = ["a", "b", "c"]
# nums3 = "abf" 不能拼接字符串
# print(nums1 + nums2)


# 列表删除操作

'''
del
作用：可以删除一个指定元素或对象
语法：del 指定元素
参数：无 
返回值：无
注意：可以删除整个列表、某个元素、一个变量
'''
# nums = [1, 2, 3, 4, 5]
# 删除某个元素
# del nums[0]
# 删除整个列表
# del nums
# print(nums)
# 删除一个变量
# num = 666
# del num
# print(num)

'''
pop
作用：移除并返回列表中指定索引对应元素
语法：list.pop(index = -1)
参数：index默认是-1，即最后一个元素
返回值：被删除元素
注意：会直接修改原数组，注意越界
'''
# nums = [1, 2, 3, 4, 5]
# print(nums.pop(2))
# print(nums)

'''
remove
作用：移除列表中指定元素
语法：list.remove(object)
参数：object是待移除的元素 
返回值：None
注意：会直接修改原数组，如果不存在，报错，存在多个，删除最左边一个，注意循环内删除列表元素的坑
'''
# nums = [1, 2, 2, 3, 4, 5]
# print(nums.remove(2))
# print(nums)
# nums2 = [1, 2, 2, 3, 4, 5, 2]
#
# for num in nums2:
#     print(num)
#     if num == 2:
#         nums2.remove(2)
# print(nums2)

# 列表修改操作

'''
通过下标修改指定列表的指定索引处的值
'''
# nums = [1, 2, 3, 4, 5]
# nums[2] = 6
# print(nums)

# 列表查询
#
# 获取单个，元素通过下标（索引）查询
nums = [1, 2, 3, 4, 5, 5, 2, 6, 6]
print(nums[2])

# 获取元素索引 list.index(value,start,stop)
print(nums.index(5, 5, 6))

# 获取指定元素个数 count()
print(nums.count(5))

# 切片与字符串一样
print(nums[1:4:1])
print(nums[-1:-4:-2])
