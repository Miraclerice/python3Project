# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 21:02:10

class Person:
    pass


p = Person()
p2 = Person()
print(p)
# print(id(p))
# print(hex(id(p)))

print(id(p), id(p2))

num1 = 10
num2 = 10
print(id(num1), id(num2))

p.name = 100


'''
1. 在Python中万物皆对象
	* 不存在基本数据类型
	* 0,  1.2,  True, False, "abc",这些全都是对象
2. 所有对象, 都会在内存中开辟一块空间进行存储
	* 会根据不同的类型以及内容, 开辟不同的空间大小进行存储
	* 返回该空间的地址给外界接收(称为"引用"), 用于后续对这个对象的操作
		a.可通过id()函数获取内存地址(10进制)
		b.通过hex()函数可以查看对应的16进制地址
3. 对于整数和短小的字符, Python会进行缓存; 不会创建多个相同对象;此时, 被多次赋值, 只会有多份引用
4. 容器对象, 存储的其他对象, 仅仅是其他对象的引用, 并不是其他对象本身
	* 比如字典, 列表, 元组这些"容器对象"
	* 全局变量是由一个大字典进行引用;global()查看
'''
