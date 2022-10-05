# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 14:30:06

# 获取文件名称列表
import os
import shutil

path = "../file"
if not os.path.exists(path):
    exit()

os.chdir(path)
file_list = os.listdir("/")
# print(file_list)
# 1 遍历所有文件
for file_name in file_list:
    # print(file_name)
    # 2 分解文件后缀名
    # 2.1获取最后一个.的索引位置
    index = file_name.rfind(".")
    # print(index)
    # 2.2根据这个索引开始截取后续内容
    extension = file_name[index + 1:]
    # print(extension)
    if extension == -1:
        continue

    # 3 查看一下， 是否存在同名的目录
    # 4 如果不存在这样的目录，创建该名称的目录
    if not os.path.exists(extension):
        # 创建
        os.mkdir(extension)
    # 移动
    # 5 目录存在后，移动对应文件
    shutil.move(file_name, extension)


