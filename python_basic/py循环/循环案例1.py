# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 15:36:32

while True:
    num1 = float(input("请输入数字num1:\n"))
    num2 = float(input("请输入数字num2:\n"))

    if num1 > 100 or num2 > 100:
        print("请重新输入\n\n")
        continue

    result = num1 + num2

    print(result)

    isQuit = input("q ： 退出，按下其他则继续\n")

    if isQuit == 'q':
        break
