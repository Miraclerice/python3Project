# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 17:03:31

# 给发说说的函数增加额外功能
# 1.不能修改函数名
# 2.不能修改函数体内部代码

def check(func):
    print("check执行了")
    def inner():
        print("登录验证操作....")
        func()
    return inner


# 使用@check立马执行check方法
@check
def publish_novels():
    print("发说说")


publish_novels()