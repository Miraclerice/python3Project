# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 11:11:36

class Person:
    __age = 12
    def __get(self):
        print("get")
    # 有问题，覆盖解释器名字重整机制
    # def _Person__get(self):
    #     print("不能这样定义")

p = Person()
# p.__get()
print(Person.__dict__)
p._Person__get()
'''
私有方法
	def __方法():
	pass
注意
	不要定义 "_类名__方法名" 这种方法,会把名字重整机制的方法覆盖掉
'''
