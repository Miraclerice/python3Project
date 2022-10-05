# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 13:04:55
f = open("a.txt", "a")
if f.writable():
    print(f.write("abc"))

    f.flush()
f.close()