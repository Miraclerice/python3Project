# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 14:55:39

username = 'admin'
password = '123456'
while True:
    usernameInput = input('请输入用户名:\n')
    passwordInput = input('请输入密码:\n')

    if username == usernameInput and passwordInput == password:
        print('登录成功')
        break
    elif username != usernameInput and passwordInput != password:
        print("用户名和密码都错误，请重新输入")
    elif username != usernameInput:
        print("用户名错误，请重新输入")
    else:
        print('密码错误，请重新输入')
