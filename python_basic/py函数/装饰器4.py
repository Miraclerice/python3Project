# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 17:13:22

# decorator 装饰器叠加使用，加@decorator方法的注解，从上往下执行
def decorator_line(func):
    def inner():
        print("-" * 100)
        func()

    return inner


def decorator_star(func):
    def inner():
        print("*" * 100)
        func()

    return inner


@decorator_line
# content = decorator_line(content)
@decorator_star
# content = decorator_star(content)
def content():
    print("社会我小谢，人狠话不多")


content()
