# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 23:01:47


# res = 0
#
#
# def first_value(value):
#     global res
#     res = value
#
#
# def add_method(value):
#     global res
#     res += value
#
#
# def sub_method(value):
#     global res
#     res -= value
#
#
# def mut_method(value):
#     global res
#     res *= value
#
#
# def div_method(value):
#     global res
#     res //= value


# first_value(100)
# add_method(100)
# sub_method(50)
# mut_method(3)
# div_method(150)
# print(res)

# -----------------优化----------------
# class Calc:
#     __res = 0
#
#     @classmethod
#     def first_value(cls, value):
#         cls.__res = value
#
#     @classmethod
#     def add_method(cls, value):
#         cls.__res += value
#
#     @classmethod
#     def sub_method(cls, value):
#         cls.__res -= value
#
#     @classmethod
#     def mut_method(cls, value):
#         cls.__res *= value
#
#     @classmethod
#     def div_method(cls, value):
#         cls.__res //= value
#
#     @classmethod
#     def show_value(cls):
#         print(f"计算结果是{cls.__res}")
#
#
# Calc.first_value(100)
# Calc.add_method(50)
# Calc.sub_method(30)
# Calc.mut_method(3)
# Calc.div_method(120)
# Calc.show_value()


# -----------------继续优化----------------

# class Calc:
#     def __init__(self, num):
#         if not isinstance(num, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#         self.__res = num
#
#     def add_method(self, value):
#         if not isinstance(value, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#         self.__res += value
#
#     def sub_method(self, value):
#         if not isinstance(value, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#         self.__res -= value
#
#     def mut_method(self, value):
#         if not isinstance(value, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#         self.__res *= value
#
#     def div_method(self, value):
#         if not isinstance(value, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#         self.__res //= value
#
#     def show_value(self):
#         print(f"计算结果是{self.__res}")
#
#
# calc = Calc(100)
# calc.add_method(56)
# calc.sub_method(30)
# calc.mut_method(3)
# calc.div_method(120)
# calc.show_value()


# -----------------继续优化----------------

# class Calc:
#     def check_num(self, num):
#         if not isinstance(num, int):
#             raise TypeError("类型错误，应该是一个整型数据")
#
#     def __init__(self, num):
#         self.check_num(num)
#         self.__res = num
#
#     def add_method(self, value):
#         self.check_num(value)
#         self.__res += value
#
#     def sub_method(self, value):
#         self.check_num(value)
#         self.__res -= value
#
#     def mut_method(self, value):
#         self.check_num(value)
#
#         self.__res *= value
#
#     def div_method(self, value):
#         self.check_num(value)
#         self.__res //= value
#
#     def show_value(self):
#         print(f"计算结果是{self.__res}")
#
#
# calc = Calc(100)
# calc.add_method(56)
# calc.sub_method(30)
# calc.mut_method(3)
# calc.div_method("120")
# calc.show_value()

# -----------------继续优化----------------

# class Calc:
#     def check_num_decorator(func):
#         def inner(self, num):
#             if not isinstance(num, int):
#                 raise TypeError("类型错误，应该是一个整型数据")
#             return func(self, num)
#
#         return inner
#
#     @check_num_decorator
#     def __init__(self, num):
#         self.__res = num
#
#     @check_num_decorator
#     def add_method(self, value):
#         self.__res += value
#
#     @check_num_decorator
#     def sub_method(self, value):
#         self.__res -= value
#
#     @check_num_decorator
#     def mut_method(self, value):
#         self.__res *= value
#
#     @check_num_decorator
#     def div_method(self, value):
#         self.__res //= value
#
#     def show_value(self):
#         print(f"计算结果是{self.__res}")
#
#
#
# calc = Calc(100)
# calc.add_method(56)
# calc.sub_method(30)
# calc.mut_method(3)
# calc.div_method(120)
# calc.show_value()

# -----------------继续优化----------------
# # 私有装饰器
# import win32com.client
# # 创建播报器对象(window系统适用)
# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # 通过播报器对象，播报语音字符串
# # speaker.Speak("你好,小谢")
#
#
# class Calc:
#     def __say(self, word):
#         # 创建播报器对象(window系统适用)
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         # 通过播报器对象，播报语音字符串
#         speaker.Speak(word)
#
#     def __check_num_decorator(func):
#         def inner(self, num):
#             if not isinstance(num, int):
#                 raise TypeError("类型错误，应该是一个整型数据")
#             return func(self, num)
#
#         return inner
#
#     @__check_num_decorator
#     def __init__(self, num):
#         self.__say(num)
#         self.__res = num
#
#     @__check_num_decorator
#     def add_method(self, value):
#         self.__say(value)
#         self.__res += value
#
#     @__check_num_decorator
#     def sub_method(self, value):
#         self.__say(value)
#         self.__res -= value
#
#     @__check_num_decorator
#     def mut_method(self, value):
#         self.__say(value)
#         self.__res *= value
#
#     @__check_num_decorator
#     def div_method(self, value):
#         self.__say(value)
#         self.__res //= value
#
#     def show_value(self):
#         str1 = f"计算结果是{self.__res}"
#         self.__say(str1)
#         print(str1)
#
#
# calc = Calc(100)
# calc.add_method(56)
# calc.sub_method(30)
# calc.mut_method(3)
# calc.div_method(120)
# calc.show_value()

# 外部函数调用，不会传本身，所以有多个参数传入报错
# def test(self, n):
#     print("jjj")
#
# calc.check_num_decorator(test)

# # -----------------继续优化----------------
# # 私有装饰器
# import win32com.client
#
#
# # 创建播报器对象(window系统适用)
# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # 通过播报器对象，播报语音字符串
# # speaker.Speak("你好,小谢")
#
#
# class Calc:
#     def __say_decorator(func):
#         def inner(self, word):
#             # 创建播报器对象(window系统适用)
#             speaker = win32com.client.Dispatch("SAPI.SpVoice")
#             # 通过播报器对象，播报语音字符串
#             speaker.Speak(word)
#             return func(self, word)
#
#         return inner
#
#     def __check_num_decorator(func):
#         def inner(self, num):
#             if not isinstance(num, int):
#                 raise TypeError("类型错误，应该是一个整型数据")
#             return func(self, num)
#
#         return inner
#
#     @__check_num_decorator
#     @__say_decorator
#     def __init__(self, num):
#         self.__res = num
#
#     @__check_num_decorator
#     @__say_decorator
#     def add_method(self, value):
#         self.__res += value
#
#     @__check_num_decorator
#     @__say_decorator
#     def sub_method(self, value):
#         self.__res -= value
#
#     @__check_num_decorator
#     @__say_decorator
#     def mut_method(self, value):
#         self.__res *= value
#
#     @__check_num_decorator
#     @__say_decorator
#     def div_method(self, value):
#         self.__res //= value
#
#     # @__say_decorator
#     def show_value(self):
#         str1 = f"计算结果是{self.__res}"
#         print(str1)
#
#
# calc = Calc(100)
# calc.add_method(56)
# calc.sub_method(30)
# calc.mut_method(3)
# calc.div_method(120)
# calc.show_value()


# -----------------继续优化----------------
# 私有装饰器
import win32com.client


# 创建播报器对象(window系统适用)
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# 通过播报器对象，播报语音字符串
# speaker.Speak("你好,小谢")


class Calc:

    # 注意这里需要有self参数
    def __say_decorator(self, word):
        # 创建播报器对象(window系统适用)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # 通过播报器对象，播报语音字符串
        speaker.Speak(word)

    def __create_say_decorator(operator_sign=""):
        def say_decorator(func):
            def inner(self, num):
                self.__say_decorator(operator_sign + str(num))
                return func(self, num)

            return inner

        return say_decorator

    def __check_num_decorator(func):
        def inner(self, num):
            if not isinstance(num, int):
                raise TypeError("类型错误，应该是一个整型数据")
            return func(self, num)

        return inner

    @__check_num_decorator
    @__create_say_decorator()
    def __init__(self, num):
        self.__res = num

    @__check_num_decorator
    @__create_say_decorator("加上")
    def add_method(self, value):
        self.__res += value
        return self

    @__check_num_decorator
    @__create_say_decorator("减去")
    def sub_method(self, value):
        self.__res -= value
        return self

    @__check_num_decorator
    @__create_say_decorator("乘以")
    def mut_method(self, value):
        self.__res *= value
        return self

    @__check_num_decorator
    @__create_say_decorator("除以")
    def div_method(self, value):
        self.__res //= value
        return self

    # @__say_decorator
    def show_value(self):
        str1 = f"小谢牌子计算结果是{self.__res}"
        self.__say_decorator(str1)
        print(str1)
        return self

    def clear(self):
        self.__res = 0
        return self

    @property
    def result(self):
        return self.__res


# calc = Calc(100)
# calc.add_method(56).sub_method(30).mut_method(3).div_method(120).show_value().clear().sub_method(200).show_value()
# print(calc.result)
