# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 21:19:56

# a = 10
# def test():
#     g = 11
#     print(a)
#     def test2():
#         print(g)
#         c = 111
#     return test2
#
#
# # print(c)
#
# test()
# # print(g)
#
# if 1 < 2:
#     aa = 10
#     print(aa)
# print(aa)

# while True:
#     a = 10
#     break
#
# print(a)

# G
# 局部变量
# b = 999
# a = 666
# def test():
#     # E
#     # a = 10
#     # a = 11
#     print(a)
#     # print(b)
#     def test2():
#         # L
#         # nonlocal a
#         # a = 100
#         print(a)
#         # print(b)
#     test2()
#     print(a)
#
# test()
#  name 'a' is not defined
# print(a)

g_a = 666
def test():
    # E
    global g_a
    g_a = 10
    print(g_a)
    # {}
    b = 10
    c = 10
    print(locals())

print(globals())
# print(a)
test()
# print(a)