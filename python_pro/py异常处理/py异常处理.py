# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/6/0006 22:09:46


# 1 / 0
# ZeroDivisionError
# # print(name)
# NameError
# num  = 10
# if num != 0:
#     print(10 / num)

# try:
#     print(name)
# except NameError:
#     print("名字没有定义")
# print(123)

# try:
#     1 / 0
#     print(name)
# except ZeroDivisionError as zero:
#     print("cc", zero)
# except NameError as ne:
#     print("名称异常", ne)
# except (ZeroDivisionError, NameError) as e:
#     print("xxx", e)
# except Exception as e:
#     print("xxx", e)
# else:
#     print(True)
# finally:
#     print("zuihou")

try:
    f = open("m5.jpg", "r")
    f.readlines()
except Exception as e:
    print(e)
finally:
    print("ccc")
    f.close()

# 但是以上写法过于繁琐, 于是有了这个方案
# 如果产生了异常, 依然会报错; 并没有进行异常处理操作
with open("m5.jpg", "r") as f:
    f.readlines()

'''
方式一处理异常
try:
    # 这里不管以后会抛出多少个异常, 只会从上往下检测, 检测到一个后, 就立即往下去匹配, 不会多次检测
    可能会出现异常的代码
except 你要捕捉的异常类别 as(Python3使用as, python使用英文逗号) 接收异常的形参:
    # 这一块可以有多个重复, 用于捕捉可能的其他异常; 如果针对于多个不同的异常有相同的处理方式, 那么可以将多个异常合并,通过写出元组合并
    对于这个异常的处理
else:
    # 这一块必须放在上一块except结束后(可以省略)
    没出现异常时做的处理
finally:
    # 这一块必须放最后(可以省略)
    不管有没有出现异常, 都会执行的代码
    
注意：
    try语句没有捕获到异常，先执行try代码段后，在执行else，最后执行finally
    如果try捕获异常，首先执行except处理错误，然后执行finally
    如果异常名称不确定, 而又想捕捉, 可以直接写Exception
'''

'''
错误
    没法通过其他的代码进行处理的问题
    语法错误
        比如定义函数写成了 dfe xxx()
        这种错误, 可以直接通过IDE或者解释器给出的提示进行修改
    逻辑错误
        语法层面没有问题, 但是自己设计的逻辑出现问题
        例如
            用户输入年龄, 判定是否成年
            if age < 18:
    print("已经成年")
        这种错误, IDE或者解释器无法帮我们检测出, 只有我们通过代码测试进行排查
'''

'''
除零异常
    示例代码
        1 / 0
    异常名称
        ZeroDivisionError
名称异常
    示例代码
        sz
    异常名称
        NameError
类型异常
    示例代码
        "1" + 2
    异常名称
        TypeError
索引异常
    示例代码
        l = [1, 2]
l[3]
    异常名称
        IndexError
键异常
    示例代码
        dic = {"name": "sz", "age": 18}
dic["add"]
    异常名称
        KeyError
值异常
    示例代码
        int("abc")
    异常名称
        ValueError
属性异常
    示例代码
        name = "sz"
print(name.xx)
    异常名称
        AttributeError
迭代器异常
    示例代码
        it = iter([1, 2])
print(next(it))
print(next(it))
print(next(it))
    异常名称
        StopIteration
'''
