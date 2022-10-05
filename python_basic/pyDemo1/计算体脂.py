# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 11:44:02

height = float(input('请输入您的身高(m)'))
weight = float(input('请输入您的体重(kg)'))
sex = int(input('请输入您的性别(sex == "男" ? 1 : 0)'))
age = int(input('请输入您的年龄'))

BMI = weight / (height * height)
TZL = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex

minNUm = 0.15 + 0.1 * (1 - sex)
maxNUm = 0.18 + 0.1 * (1 - sex)

result = minNUm < TZL < maxNUm
print('体脂率是%f' % TZL)
print('体脂率是否符合标准', result)
