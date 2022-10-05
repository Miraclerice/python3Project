# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 14:57:29

# 打印文件目录文件夹及文件清单
# 获取文件名称列表
import os
import shutil

# path = "../file"
# if not os.path.exists(path):
#     exit()
# listdir = os.listdir(path)
# print(listdir)

def listFiles(dir, f):
    file_list = os.listdir(dir)
    # print(file_list)
    for file_name in file_list:
        new_file_name = dir + "/" + file_name
        # 判断是不是目录
        if os.path.isdir(new_file_name):
            # print(new_file_name)
            f.write(new_file_name + "\n")
            # 是目录，递归
            listFiles(new_file_name, f)
        else:
            # print("\t" + file_name)
            f.write("\t" + file_name + "\n")

    # print("")
    f.write("\n")


f = open("list.txt", "a")
listFiles("../file", f)