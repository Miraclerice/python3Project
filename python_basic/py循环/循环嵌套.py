# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 15:45:22

# for i in range(1, 6):
#     for j in range(1, 3):
#         print(i*j)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i * j,end="\t")
    print()
