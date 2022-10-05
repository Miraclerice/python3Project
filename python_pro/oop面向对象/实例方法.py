# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/4/0004 20:19:52

class Person:
    def eat(self, food):
        print("吃" + food, self)

    def eat2(a):
        print(a)

    # def eat2():
    #     print()


person = Person()
person.eat2()
# print(person)
# person.eat("西瓜")

# print(Person.eat)
# Person.eat(123, "kk")
# func = Person.eat
# func(12, "ll")
'''
class 类名:
    def 方法名(self):
        方法体

标准调用：
    使用实例调用实例方法，不用手动传参，解释器默认将当前实例本身传递过去
    注意：至少有一个参数，不然报错，一般形参用self，也可以自定义
其他调用：
    使用类调用: 类名.方法名(参数列表)
    间接调用: 函数名 = 类名.方法名   函数名(参数列表)
    本质就是找到函数本身取调用它
'''