# _*_ coding: UTF-8 _*_
# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 18:08:13

# 生成器
# l = [i for i in range(10000000) if i % 2 == 0]
# 生成器创建方式一：
# l = (i for i in range(10000000) if i % 2 == 0)
# print(l)
# print(next(l))
# print(next(l))
# print(next(l))
# print(l.__next__())
# for i in l:
#     print(i)

# 生成器方式二：
# yield，可以阻断当前函数执行，当使用next(generator)或者generator.__next__()函数，让函数继续执行，当执行下一个yield时，又阻断
# def test():
#     print("test函数执行")
#     # 遇到yield，阻断执行
#     yield 1
#     print("a")
#
#     yield 2
#     print("b")
#
#     yield 3
#     print("c")
#
#     yield 4
#     print("d")
#
#     yield 5
#     print("e")
#
# def test():
#     for i in range(1, 9):
#         yield i
#         # print("a" + str(i))
#
#
# g = test()
# print(g, type(g))

# print(next(g))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# num = int(input("三位数\n"))
# if 100 <= num <= 999:
#     print(str(num) + "是一个三位整数", type(num))
# if num // 100 != 0 and num // 1000 == 0:
#     print("xxx")
#
# num = float(input("三位数\n"))
# if 100 <= num <= 999:
#     print(str(num) + "是一个三位整数", type(num))
# if num // 100 != 0 and num // 1000 == 0:
#     print("xxx")


# def test():
#     print("test函数执行")
#     res1 = yield 1 # "000"
#     print(res1)
#
#     res2 = yield 2
#     print(res2)
#
#
# g = test()
# # 开启调用函数
# print(g.__next__())
# # print(g.__next__())
# # g.__next__(),默认是None,使用g.send("000")可以给上一次挂起的yield传值
# print(g.send("000"))
# print(g.send(None))

# def test():
#     yield 1
#     print("a")
#     return 10
#     yield 2
#     print("b")
#     yield 3
#     print("c")
#
#
# g = test()
# print(g.__next__())
# print(g.__next__())
# # 关闭生成器
# g.close()
# print(g.__next__())
# g = test()
# for v in g:
#     print(v)

while True:
    str1 = input("三位数\n")
    if (str1.find('.') == -1):
        num = int(str1)
        if 100 <= num <= 999:
            print(str(num) + "是一个三位整数", type(num))
        if num // 100 != 0 and num // 1000 == 0:
            print(str(num) + "是一个三位整数", type(num))
    else:
        print("不是三位整数")
