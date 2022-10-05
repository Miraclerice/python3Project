# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 13:21:29

import os

# 重命名文件  os.rename(原, 新)， 没有文件或目录报错
# os.rename("b.txt", "one.txt")

# 重命名目录
# os.rename("first", "one")

# 同时修改目录名和文件名  renames()
# os.renames("one/one.txt", "two/two.txt")

# 删除文件,不存在报错  remove()
# os.remove("m52.jpg")

# 删除目录，文件夹非空报错  rmdir()
# os.rmdir("one")

# 只删除two目录
# os.rmdir("one/two")

# 递归删除目录，文件夹非空报错  removedirs()
# os.removedirs("one/two")

# 创建一级目录 mkdir()
# os.mkdir("one")

# 无法递归创建多级目录，报错
# os.mkdir("a/b/c")

# os.mkdir("a", 0o777)
'''
数字权限模式,windows忽略，可以参照linux的文件权限(读r:4、写w:2、可执行x:1)
文件拥有者 八进制第一位数(读r:4、写w:2、可执行x:1)
同组用户   八进制第二位数(读r:4、写w:2、可执行x:1)
其他用户   八进制第三位数(读r:4、写w:2、可执行x:1)
'''

# 切换默认目录,os.chdir(target目录)，目标目录不存在会报错
# os.chdir("one")

# open("ddd.txt", "w")
# 获取当前目录 os.getcwd()
# print(os.getcwd())

# 获取目录内容列表  os.listdir(path) 目录默认是当前目录下("./") 返回一个列表
print(os.listdir("../../"))
