# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 22:24:23

class Person:
    """
    关于这个类的描述，类的作用，类的构造函数等等；类属性的描述
    直接在类的下方,使用三个 "双引号"对就可以
    需要注明类的作用, 以及类属性描述
    至于方法, 则直接在方法下,使用三个"双引号"对描述即可
	作用参数返回值
    """
    age = 10

    def run(self):
        """
        :a 啊
        :return:
        """
        print("kkk")
        a = 100
        return a


help(Person)

'''
方式1:
使用内置模块pydoc
具体步骤
    1.查看文档描述
        python -m pydoc 模块名称
    2.启动本地服务, 浏览文档
        python -m pydoc -p 1234
        # 自动生成端口号
        python -m pydoc -b
    3.生成指定模块html文档
        python -m pydoc -w 模块名称
方式2
使用三方模块
    Sphinx
    epydoc
    doxygen
'''