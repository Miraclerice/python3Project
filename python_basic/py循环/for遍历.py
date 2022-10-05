# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 15:14:13

notice = '你好屌哦，弟弟'
for c in notice:
    print(c)

pets = ['小昭', '小黄', '小妹']
for pet in pets:
    print(pet)
    # break
else:
    print('over')


# 反转字符串
notice1 = "我是牛马，没人是我对手"
result = ""
for c in notice1:
    result = c + result
print(result)

# 打印1-100 rang(1, 100) [1, 100]
for c in range(1, 101):
    if c % 2 == 0:
        print(c)
