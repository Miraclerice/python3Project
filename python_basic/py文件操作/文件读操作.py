# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 12:40:04
from collections.abc import Iterator

f = open("a.txt", "r")
# f.seek(2)
# content = f.read(2)
# print(f.tell())
# print(content)
# print("文件指针位置 : ", f.tell())
# print(f.readline(), end="")
# print("文件指针位置 : ", f.tell())
# print(f.readline(), end="")
# print("文件指针位置 : ", f.tell())
# print(f.readline(), end="")
# print("文件指针位置 : ", f.tell())
# print(f.readline(), end="")
# print("文件指针位置 : ", f.tell())
# print(f.readline(), end="")

# 判断是不是迭代器
# print(isinstance(f, Iterator))
# for c in f:
#     print(c, end="")

if f.readable():
    content = f.readlines()
    print(content)

    for c in content:
        print(c, end="")


'''
f.read(字节数)
    字节数默认是文本内容长度，下标自动移动
* f.readline([limit])
    读取一行数据，limit限制最大读取字节数
f.readlines()
    自动将文件按照换行符处理，将处理好的每一行数据组成列表返回
    
* for in (动态加载内存)
    1.遍历行列表
    2.遍历文件本身(文件对象就是迭代器）

判断文件是否可读(容错处理)
    file对象.readable()

注意：
    文件比较大时使用readline方法，按行加载，可节省内存，但相对于其他两个读取方法，性能较低
    其他两个方法一次读取全部内容，虽然占用内存，但处理性能比较高
'''

f.close()
