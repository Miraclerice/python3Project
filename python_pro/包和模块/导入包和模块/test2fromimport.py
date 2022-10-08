# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 15:03:48

# from other import name2 as nm2
#
# print(nm2)

# 从包中导入多个模块并起别名
# from p1 import tool_module as tm, tool_module2 as tm2
#
# print(tm.name)
# print(tm2.name)

# 体现从包中导入多个模块并起别名的包的层级性
# from p1.sub_module import tool_module2 as tm, pmodule as p
# print(tm.name, p.name)

# 从模块中导入多个模块资源并起别名
# from p1.tool_module import name as n, sex as s
# print(s, n)

from other import *
print(name)
print(name2)
print(name3)
print(name4)
# print(_name5)
# print(__name6)

from p1 import *
print(tool_module.name)
print(tool_module2.name)
# 列表没有
# print(tool_module3.name)
'''
语法：
    from A import B[ as 别名]
    A的资源必须包含B，即A顺序在前
资源排序：
    包 > 模块 > 模块资源
注意面向关系：
    包只能看到模块，看不到模块资源
    模块只能看到模块资源
    
最终组合：
    1.从包中导入导入模块（包是可能有层级关系，模块没有层级，但可以多个，可以起别名）
    2.从模块中导入导入模块资源（模块是可能有层级关系(包有层级的)，模块资源没有层级，但可以多个，可以起别名）
    
注意：保持import后面最简化，即所有层级关系放在from后面

特例：
    1.from 模块 import *
    "*"代表所有非下划线_开头资源导入到当前位置(定义__all__看列表的，这个规定需要看列表有没有写入来判断)
    与在引入模块声明的__all__ = ["资源1", "资源2", ...]配合使用，代表"*"匹配到的资源，注意列表内都是字符串
    注意：慎用，避免当前位置与导入资源的变量冲突
    
    2.from 包 import *
    与在引入包的__init__.py中声明的__all__ = ["资源1", "资源2", ...]配合使用，代表"*"匹配到的模块，注意列表内都是字符串
    必须写__all__,没有什么都不导入
'''
