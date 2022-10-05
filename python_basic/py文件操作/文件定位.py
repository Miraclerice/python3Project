# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 12:08:56
f = open("a.txt", "rb")
# f = open("py文件操作/a.txt", "r")

# 查看文件指针位置
print(f.tell())
f.seek(5)
# 文件指针偏移
f.seek(-2, 1)
print(f.tell())

print(f.read())

print(f.tell())

f.close()
