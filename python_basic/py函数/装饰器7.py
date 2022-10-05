# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 17:50:49

# 获取装饰器，通过char控制获取不同装饰器
def getDecorator(char):
    def decorator(func):
        def inner():
            print(char * 50)
            func()

        return inner

    return decorator


@getDecorator("*")
def fp():
    print("中华人民共和国万岁")


fp()
