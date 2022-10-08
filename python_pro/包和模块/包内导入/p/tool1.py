# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 20:02:08

# import tool2
# import other

# from p import tool2
# from .. import tool2
from . import tool2


def run():
    print(tool2.name)
    print(tool2.sex)

print(__name__)
