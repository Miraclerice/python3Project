# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 17:22:44

# 对有参函数进行装饰
def decorator(func):
    def inner(*args, **kwargs):
        print("*" * 50)
        print(args, kwargs)
        # 拆包
        func(*args, **kwargs)

    return inner


@decorator
def print_number(num1, num2, num3):
    print(num1, num2, num3)


@decorator
def print_number2(num1):
    print(num1)


print_number(123, 666, num3=666)
print_number2(123)
