# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 22:15:20

# 读操作
# 1.打开文件，返回文件对象
# 相对路径，相对哪一个目录下的指定文件
# f = open("a.txt", "r")
# # 2.读写操作
# content = f.read()
# print(content)
#
# # f.write("123456")
#
# # 3.关闭文件
# f.close()


# 写操作
# 1.打开文件，返回文件对象
# 相对路径，相对哪一个目录下的指定文件
# f = open("a.txt", "w")
#
# # 2.读写操作
# # not readable 不能读，覆盖原文件
# # f.write("abcdefghijklmnopqrstuvwxyz")
# f.write("123")
#
# # 3.关闭文件
# f.close()


# 追加操作
# 1.打开文件，返回文件对象
# 相对路径，相对哪一个目录下的指定文件
f = open("a.txt", "a")

# 2.读写操作
# not readable
# print(f.read())
f.write("abcdefghijklmnopqrstuvwxyz")

# 3.关闭文件
f.close()