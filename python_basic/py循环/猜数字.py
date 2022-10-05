# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 16:14:14
# from random import random
import random

target = random.randint(1, 200)
count = 0
allChance = 5
while True:
    count += 1
    num = input("请输入一个数字：\n")
    num = int(num)
    if num == target:
        print("猜对了，猜了%d次" % count)
        break
    elif count <= allChance:
        if num > target:
            print("猜大了，重新猜，还有%d次机会" % (allChance - count))
        else:
            print("猜小了，重新猜，还有%d次机会" % (allChance - count))
    if count >= allChance:
        break
