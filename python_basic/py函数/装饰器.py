# _*_ coding: UTF-8 _*_
# @author  : M_Xie
# @date    : 2022/10/3/0003 16:24:17

# 装饰器
# 开放封闭原则：已经写好的代码，尽可能不要修改，如果想新增功能，在原来代码基础上，单独进行扩展
# 单一职责原则：单一功能

def publish_novels():
    # print("login_check")
    login_check()
    print("发说说")


def publish_pictures():
    # print("login_check")
    login_check()
    print("发图片")


def login_check():
    print("login_check")


# 业务逻辑代码
btn = 2
if btn == 1:
    # print("login_check")
    publish_novels()
else:
    # print("login_check")
    publish_pictures()

# 方式一：在业务逻辑代码添加登录验证代码，代码冗余度大，维护性能差
# 方式二：在功能函数添加登录验证代码，减少代码重复度,复用性好
