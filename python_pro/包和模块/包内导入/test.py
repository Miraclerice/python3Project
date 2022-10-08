# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 19:23:45

# __name__
# 如果一个py文件直接以脚本形式执行 python file，它的名称就是__main__
# 如果一个py文件使用模块的形式，进行加载的，那么它的名称由加载路径决定的，包名(顶级名称).子包名.模块名
from p import tool1
import sys
print(sys.path)
tool1.run()
print("-" * 50)
print(__name__)