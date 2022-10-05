# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 23:25:21


# 操作
# 1.打开xx.jpg，取出内容，获取文件内容的前半部分
# 1.1 打开文件
# fromfile = open("m5.jpg", "rb")
#
# # 1.2 读取内容
# fromcontent = fromfile.read()
# print(fromcontent)
#
# # 1.3 关闭文件
# fromfile.close()
#
# # 2.打开xx2.jpg，然后把取出的半部分内容，获写入放到xx2.jpg中
# # 2.1 打开目标文件
# tofile = open("m52.jpg", "wb")
#
# # 2.2 写入操作
# tofile.write(fromcontent[0:len(fromcontent) // 2])
#
# # 2.3 关闭文件
# tofile.close()

# 操作rb+
# 1.打开xx.jpg，取出内容，获取文件内容的前半部分
# 1.1 打开文件
fromfile = open("m5.jpg", "rb+")

# 1.2 读取内容
fromcontent = fromfile.read()
print(fromcontent)

# 1.3 关闭文件
fromfile.close()

# 2.打开xx2.jpg，然后把取出的半部分内容，获写入放到xx2.jpg中
# 2.1 打开目标文件
tofile = open("m52.jpg", "wb+")

# 2.2 写入操作
tofile.write(fromcontent[0:len(fromcontent) // 2])

# 2.3 关闭文件
tofile.close()