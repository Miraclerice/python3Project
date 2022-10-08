# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 23:16:19
# import traceback
# class Test(object):
#     def __enter__(self):
#         print("enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self, exc_type, exc_val, exc_tb)
#         print(traceback.extract_tb(exc_tb))
#         print("exit")
#         # True 不显示异常信息， False:显示异常信息
#         return True
#
# with Test() as x:
#     # print("body", x)
#     1 / 0

# '''
# 定义的类, 实现"上下文管理协议"
#     __enter__
#         做一些预处理操作
#     __exit__
#         做一些清理操作
#         接收抛出的异常
#         如果返回True, 则忽略异常; 如果返回的False, 则再次抛出异常
# '''
import contextlib

# @contextlib.contextmanager
# def test():
#     # __enter__方法的具体实现
#     print(1)
#     # __exit__方法的具体实现
#     yield "kkkk"
#     print(2)
#
#
# with test() as x:
#     print(3, x)

# @contextlib.contextmanager
# def ze():
#     try:
#         yield
#     except Exception as e:
#         print("error", e)
#
#
# num1 = 1
# num2 = 0
#
# with ze():
#     num1 /num2
# # try:
# #     num1 / num2
# # except Exception as e:
# #     print("666")
#
# a = 10
# b = 0
# with ze():
#     a / b


# class Test:
#     def t(self):
#         print("tttt")
#
#     # 必须写
#     def close(self):
#         print("资源释放")
#
#     # 使用contextlib.closing取代
#     # def __enter__(self):
#     #     return self
#     #
#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     self.close()
#
#
# with contextlib.closing(Test()) as test:
#     test.t()

# python2.7
# with open("m5.jpg", "rb") as from_file:
#     with open("m52.jpg", "wb") as to_file:
#         contents = from_file.read()
#         to_file.write(contents)

# python3.x
with open("m5.jpg", "rb") as from_file, open("m52.jpg", "wb") as to_file:
        contents = from_file.read()
        to_file.write(contents)

# python2.7之前
# with contextlib.nested(open("m5.jpg", "rb"), open("m52.jpg", "wb")) as (from_file, to_file):
#     contents = from_file.read()
#     to_file.write(contents)

'''
@contextlib.contextmanager
    使用装饰器, 让一个生成器变成一个"上下文管理器"
contextlib.closing
    这个函数, 让一个拥有close方法但不是上下文管理器的对象变成"上下文管理器"
contextlib.nested
    python2.7之前: 完成多个上下文管理器的嵌套
'''
