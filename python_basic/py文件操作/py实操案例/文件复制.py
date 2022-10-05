# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 14:03:03

# 文件复制案
import os

os.chdir("../file/")
# 1.以只读模式打开要复制的文件
# 以追加模式打开副本文件
# 两个文件编码一致，不会乱码
source_file = open("poem.txt", "r", encoding="utf-8")
target_file = open("poem_copy.txt", "a", encoding="utf-8")

# 2.从原文件中读取内容
# 目标文件写内容
# if source_file.readable():
# content = source_file.read()
# if target_file.writable():
# target_file.write(content)

while True:
    content = source_file.read(1024)
    if len(content) == 0:
        break
    target_file.write(content)

# 刷新流
target_file.flush()

# 3.关闭流
source_file.close()
target_file.close()
