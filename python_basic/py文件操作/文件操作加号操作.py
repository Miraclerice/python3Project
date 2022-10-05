# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 23:40:09


# r+操作
# 不管是读还是写，没有文件 No such file or directory: 'a.txt'报错
# 1.打开文件，返回文件对象
# 相对路径，相对哪一个目录下的指定文件
# f = open("a.txt", "r+")
#
#
# # 2.读写操作
# # 可以读操作，指向文件头，读取全部内容
# # print(f.read())
# # f.write("abcdefghijklmnopqrstuvwxyz")
# # 可以写入，指针指向文件头部，覆盖写入的内容长度，不会全部覆盖
# f.write("123")
#
# print(f.read())
#
# # 3.关闭文件
# f.close()

# w+操作
# 不管是读还是写,文件不存在，创建文件
# 1.打开文件，返回文件对象
# 相对路径，相对哪一个目录下的指定文件
# f = open("a.txt", "w+")


# # 2.读写操作
# # 可以读操作，指向文件头，清空全部内容
# # print(f.read())
# # f.write("abcdefghijklmnopqrstuvwxyz")
# # 可以写入，指针指向文件头部，覆盖原文件全部内容
# f.write("123")
#
# print(f.read())
#
# # 3.关闭文件
# f.close()



# a+操作
# 没有文件，件不存在，创建文件
# 1.打开文件，返回文件对象
# f = open("a.txt", "a+")
#
#
# # 2.读写操作
# # 可读，不报错
# # print(f.read())
# f.write("abcdefghijklmnopqrstuvwxyz")
# # 可以写入，指针指向文件尾，追加写入
# # f.write("123")
#
# print(f.read())
#
# # 3.关闭文件
# f.close()


# ra+操作
# 没有文件，No such file or directory报错
# 1.打开文件，返回文件对象
f = open("a.txt", "ra+")


# 2.读写操作
# 可读，返回b'内容'
# print(f.read())
# f.write("abcdefghijklmnopqrstuvwxyz")
# 可以写入，指针指向文件尾，追加写入
# f.write("123")

# print(f.read())

# 3.关闭文件
f.close()