# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 17:40:41

# 对有返回值的函数进行装饰
def decorator(func):
    def inner(*args, **kwargs):
        print("*" * 50)
        print(args, kwargs)
        # 拆包
        res = func(*args, **kwargs)
        return res

    return inner


@decorator
def print_number(num1, num2, num3):
    print(num1, num2, num3)
    return num1 + num2 + num3


@decorator
def print_number2(num1):
    print(num1)


# inner函数必须要有返回值，且与被装饰者返回值一致
res1 = print_number(123, 666, num3=666)
res2 = print_number2(123)
print(res1, res2)
