# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 15:49:43

# import other
# print(other.name)
# name = "777"
# other.run()
# print(other)
# print(id(other))
# print(type(other))
# print(other.__dict__)
# 模块对象只导入一次
# print(id(other))
# import other
# print(id(other))
# import other
# print(id(other))

#
# def test():
#     import other
#     print(other.name)
#
#
# test()
# 导入到当当前命名空间，所以没有导入，报错
# print(other.name)






# 内置模块的sys
# import sys
# print(sys.name)


# import fnmatch
# # print(fnmatch.fnmatch)
# print(fnmatch.name)


# import sys
#
# # sys.path.append(r"F:\桌面\myDir")
# import tsroute
# print(tsroute.name)
#
# print(sys.path)

# 查看当前文件路径的目录
# import os
# print(os.getcwd())
#
# # 查看特定路径
# import site
# print(site.getsitepackages())
#
# import sys
#
# print(sys.path)
# # 创建.pth文件的路径必须是全中文
# import tsroute2
# print(tsroute2.name)

# 查看已加载文件
import sys

print(sys.modules)


import other
import other
import other

print(sys.modules)