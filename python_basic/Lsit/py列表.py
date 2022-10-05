# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 22:18:21

# names = ["张三", "李四", "王五"]
# names = ["张三", 12, True]
# names = []
items = ['a', 'b', 'c']
names = ["张三", 12, True, items]
print(names, type(names))

names2 = range(1, 20, 2)
print(names2)

# nums = [1, 2, 3, 4, 5]
# 原始方式
# resNums = []
# for num in nums:
#     # print(num)
#     if num % 2 == 0:
#         continue
#     resNUm = num ** 2
#     print(resNUm)
#     resNums.append(resNUm)
# print(resNums)

# 列表推导式
nums = [1, 2, 3, 4, 5]
# resList = [num ** 2 for num in nums if num % 2 != 0]
# resList = [num ** 2 for num in nums for num2 in nums]
resList = list(num ** 2 for num in nums for num2 in nums)
print(resList)
