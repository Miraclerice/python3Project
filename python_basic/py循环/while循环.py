# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 15:08:08

num = 0
sum = 0
while num < 10:
    num += 1
    sum += num
    print(num)
    break
else:
    print(sum)