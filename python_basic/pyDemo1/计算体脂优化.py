# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 11:44:02

height = float(input('请输入您的身高(m)'))
weight = float(input('请输入您的体重(kg)'))
sex = int(input('请输入您的性别(sex == "男" ? 1 : 0)'))
age = int(input('请输入您的年龄'))

if not (0 < height < 3 and 0 < weight < 300 and 0 < age < 150 and (sex == 0 or sex == 1)):
    print('不符合条件，退出')
    exit()

BMI = weight / (height * height)
# 计算体脂率
TZL = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex
TZL /= 100

# minNUm = 0.15 + 0.1 * (1 - sex)
# maxNUm = 0.18 + 0.1 * (1 - sex)

# result = minNUm < TZL < maxNUm
result = False
# 区分男女
if sex == 1:
    result = 0.15 < TZL < 0.18
elif sex == 0:
    result = 0.25 < TZL < 0.28


# print('体脂率是%f' % TZL)
# print('体脂率是否符合标准', result)

if sex == 1:
    wenHao = '先生你好'
    minNum = 0.15
    maxNum = 0.18
elif sex == 0:
    wenHao = '女士你好'
    minNum = 0.25
    maxNum = 0.28

if result:
    notice = '恭喜你，身体健康，继续保持'
else:
    if TZL > maxNum:
        notice = '身体不正常，偏胖'
    elif TZL < minNum:
        notice = '身体不正常，偏瘦'


print(wenHao , notice)