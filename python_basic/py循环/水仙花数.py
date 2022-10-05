# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 15:52:04
while True:
    number = input('请输入三位的数：\n')
    print(len(number))
    number = int(number)
    print(number, type(number))

    if not 100 <= number <= 999:
        print("输入的数有误，不是三位的数")
        exit()
    #  符合三位数
    # 个位
    # print(number % 10)
    geWei = number % 10
    # 十位
    shiWei = number // 10 % 10
    # print(baiWei)
    # print(number % 100 // 10)
    # 百位

    baiWei = number // 100
    # print(baiWei)

    result = geWei ** 3 + shiWei ** 3 + baiWei ** 3 == number
    if result:
        print("%d 是水仙花数" % number)
        break
    else:
        print("%d 是不水仙花数" % number)
        continue

# print(number ** 2)

# for num in range(100, 1000):
#     if ((num % 10) ** 3) + ((num // 10 % 10) ** 3) + ((num // 100) ** 3) == num:
#         print(num)
