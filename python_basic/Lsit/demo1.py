# -*- coding: utf-8 -*-
# @Author  : XieBingxian
# @Time    : 2022/8/16/0016 13:30:45
# @File    : demo1.py
# @Software: PyCharm

# 标识符
import keyword
print(keyword.kwlist)

# 列表特点
# 列表元素按顺序有序排序
# 列表可以存储重复数据
# 任意数据类型混存
# 索引映射唯一数据
# 根据需要动态分配和回收内存


# 列表方式一
lst = ['孙悟空', '唐僧', '猪八戒', 0]
print(id(lst))
print(type(lst))
print(lst)
print("=====")

print(lst[0], lst[1], lst[2], lst[3])
print(lst[-3], lst[-2], lst[-1])

# 列表方式二
lst2 = list(['孙悟空', '唐僧', '猪八戒'])
print(lst2)

list1 = ['你好', '赵薇', '利丰达', '你好']
# 获取索引
print(list1.index('你好'))  # 列表中有相同元素，返回第一索引
# print(list1.index('jjjkk'))
print(list1.index('你好', 0, 3))
