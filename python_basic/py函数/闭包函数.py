# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 15:28:26

# 闭包函数
def func1():
    a = 100

    def func2():
        print(a)

    return func2


# 得到func2
newFunc = func1()


# 调用内部函数
# newFunc()


# 生成分割线
# def line_config(content, length):
#     def line():
#         print("-" * (length // 2) + content + "-" * (length // 2))
#
#     return line
#
#
# f = line_config("闭包函数", 100)
# f()
# f()
# f()
# f()

# external and internal
# def external_func():
#     num = 10
#
#     def internal_func():
#         # nonlocal关键字 非局部的
#         nonlocal num
#         num = 666
#         print(num)
#
#     # 没有加nonlocal 10
#     print(num)
#     internal_func()
#     # 没有加nonlocal 10
#     print(num)
#     return internal_func
#
#
# func = external_func()
# func()

# 闭包注意事项二
def external_func():
    num = 10

    def internal_func():
        print(num)

    num = 100

    return internal_func


func = external_func()
# 函数被调用时才确定内部变量标识对应的值
# 100
func()


def external_func1():
    funcs = []
    for i in range(1, 4):
        def internal_func1():
            print(i)

        funcs.append(internal_func1)

    return funcs


func_ = external_func1()
print(func_, type(func_))
# 全是3
func_[0]()
func_[1]()
func_[2]()


def external_func2():
    funcs = []
    for i in range(1, 4):
        def internal_func2(num):
            def inner():
                print(num)

            return inner

        funcs.append(internal_func2(i))

    return funcs


func2 = external_func2()
print(func2, type(func2))
# 1、2、3
func2[0]()
func2[1]()
func2[2]()
