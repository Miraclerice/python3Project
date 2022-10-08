# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 20:02:08

# import tool2
#  import tool2 python2.x 隐式相对导入等同于 from . import tool2
# import tool2
# 使用from __future__ import absolute_import禁用隐式相对导入
from __future__ import absolute_import
import tool2


print(tool2.name)

t1 = 10