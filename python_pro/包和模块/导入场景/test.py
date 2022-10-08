# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 18:35:02

# --------------------局部导入--------------------------
# def run():
#     """
#     局部导入
#     """
#     import other
#     print(other.name)
#     print(other.num)
#
#
# run()


# --------------------覆盖导入--------------------------
# 非内置的标准库模块重名被覆盖
# import mailbox
#
# print(mailbox.Mailbox)

# 内置的标准库模块重名被覆盖
# import sys
from python_pro.包和模块.导入场景 import sys
# print(sys.path)
print(sys.name)
