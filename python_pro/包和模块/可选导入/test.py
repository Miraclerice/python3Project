# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 19:23:45

# 优先导入other2
try:
    import other2 as o
except ModuleNotFoundError:
    import other as o

o.run()