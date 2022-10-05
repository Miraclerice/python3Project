# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 17:31:00

import random
# [0,1)
print(random.random())

seq = [1, 3, 5, 6, 9]
# 取随机索引对应的值
print(random.choice(seq))

# 随机小数[a, b]
print(random.uniform(1, 3))
# 随机整数[a, b]
print(random.randint(1, 3))

# 区间随机值[a, b)
print(random.randrange(1, 4))