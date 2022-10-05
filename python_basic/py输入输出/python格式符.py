# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 10:45:46

minute = 2
second = 3

print('%02d:%02d' % (minute, second))

ss = 8
print('% d' % ss)
print('%-6d' % ss)
print('%06d' % ss)

score = 59.39

print('%-5.2f' % score)
print('%d' % score)

englishSc = 100
mathSC = 60
print('数学成绩 ：%(ms)d, 英语成绩：%(es)d' % ({'es': englishSc, 'ms': mathSC}))

print('%d' % 0b10)
print('%d' % 0o10)
print('%d' % 0x10)
print('%o' % 10)
print('%d' % 0x10)

print('%E' % 10)
print('%g' % 12222201.1)


print('%s' % 'dsajhkh')
print('%c' % 97)
print('%c%%' % 97)
# print('%b' % 97)