# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 14:07:45
# 导入单个模块
# import other
#
# print(other.name)

# 未发布的包和模块注意通过import只能导入当前文件的目录的下的
# import p1.tool_module
# print(p1.tool_module.name)

# import p1.sub_module.pmodule
# print(p1.sub_module.pmodule.name)

# 导入多个模块
# import other, p1.tool_module, p1.sub_module.pmodule
#
# print(other.name, p1.tool_module.name, p1.sub_module.pmodule.name)

# 导入多个模块并且起别名
# import other as o, p1.tool_module as pt, p1.sub_module.pmodule as psp
#
# print(o.name, pt.name, psp.name)

import p1
# 在初始化的py文件加入import p1.tool_module
print(p1.tool_module.name)


'''
以下的包模块可以使用点语法定位
1.导入单个模块
import 同级目录的模块名/包名.模块名(注意包名可以嵌套,但是自己定义的模块与包使用这种方式导入只能导入当前py文件目录下的，不然报错找不到)

2.导入多个模块 
import 同级目录的模块名/包名.模块名, 同级目录的模块名/包名.模块名...

3.导入单个/多个模块并起别名(使用as关键字，与sql语法不同的是as不能省略)
import 同级目录的模块名/包名.模块名 as 别名, 同级目录的模块名/包名.模块名 as 别名 ... 

注意：
1.使用时，需要指定资源的模块名称，即写全，例如p1.tool_module.name
2.如果仅仅导入一个包，在__init__.py再次导入相关模块，一般使用from... import...方式导入
'''