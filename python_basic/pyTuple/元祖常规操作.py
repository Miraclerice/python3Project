# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 19:33:35

# t = ('aa', 'bb', 'cc', "dd", "ee")
# 不能删除
# del t[0]

# t[0] = "gg"
# 元祖查询
# 获取单个元素，下标法
# print(t[1])
# print(t[-1])

# 获取多个元素
# tuple[start:stop:step]
# print(t[0:3])
# print(t[::-1])

# t = ('aa', 'bb', 'cc', "dd", "ee")
# 获取
'''
tuple.count(item), 统计元组中指定元素的个数，没有返回0
tuple.index(item), 获取元组中指定元素的索引，没有报错
内建函数
len(tuple), 返回元组的元素个数
max(tuple), 返回元组的元素最大值
min(tuple), 返回元组的元素最小值
'''

# print(t.count('aaa')) #0
# print(t.count('aa')) #1

# print(t.index('bb'))  # 0
# print(t.index('bbb'))  # 报错

# print(len(t))
# print(min(t))
# print(max(t))

'''
in 判定元素是否在元组里面
not in判定元素是否不在元组里面
'''
# print('aa' in t)
# print('aa' not in t)

# 比较
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
t = ('aa', 'bb', 'cc', "dd", "ee")
t1 = ('aa', 'bb', 'cc', "dd", "ee", "ff")
# print(t > t1)
# print(t == t)
# print(t < t1)

# 元组拼接
'''
乘法拼接：tuple * int类型
加法拼接：tuple1 + tuple2
注意不同数据类型不能使用+拼接，保错

拆包
变量名1,变量名2... = (元素1,元素2,...)
括号可以省略
变量名1,变量名2... = 元素1,元素2,...

交换变量的值,也可以加括号
变量名1,变量名2 = =变量名2, 变量名1
'''
print(t * 3)
print(t + t1)
# print(t + 1)

# a, b = (10, 100)
a = 100
b = 200
a, b = b, a
print(a, b)
