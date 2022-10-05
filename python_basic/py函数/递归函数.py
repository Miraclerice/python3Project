# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 21:08:41

# 递归求n!
def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)


print(recursion(9))
