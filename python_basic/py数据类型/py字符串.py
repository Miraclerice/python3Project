# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/9/30/0030 17:58:10

# 非原始字符串
# str1 = 'dgshj'
# print(str1, type(str1))

# str1 = "dgshj"
# print(str1, type(str1))

# str1 = '''dgshj'''
# print(str1, type(str1))

# str1 = """dg\nshj"""
# print(str1, type(str1))

# str3 = "lsdjg"\
#     "sdajk"
# print(str3)

# 原始字符串
# str1 = r'dg\tsh\nj'
# print(str1, type(str1))

# str1 = "dgshj"
# print(str1, type(str1))

# str1 = '''dgshj'''
# print(str1, type(str1))

# str1 = """dg\nshj"""
# print(str1, type(str1))

# ss = "我是\"nm\""
# ss = "我是'nm'"
# print(ss)

# ss = "我是" \
#      "nm"
# ss = ("我是"
# "nm")

# 多行结果打印
# ss = '''rweayr
# awyr
# sadhy
# '''
# ss = "adsjk" + "adshfgjk"
# print(ss)

# result = "aaa" + "bbb"
# result = "aaa""bbb"
# result = "%s%s" % ("aaa", "bbb")
# result = "aaa\t" * 10
# print(result)

# a = 'hsadjg'
# print(len(a))
# print(a[0])
# print(a[-1])
# print(a[-6])
# print(a.index('h'))

# string = 'abcdefg'
# 包头不包尾
# print(string[0:3])
# print(string[::])
# print(string[0:len(string):1])
# print(string[len(string):0:-1])
# print(string[::-1])
# print(string[-1:-(len(string) + 1):-1])


# string = 'abcdefg\na'
# 获取字符串长度
# print(len(string))

# 查找方法
# 对象.find(目标片段, 起始值, 结束值) 找到返回指定索引，找不到返回-1
# print(string.find('c', 0, 1))
# print(string.rfind('c', 0, len(string)))

# print(string.index('a'))
# print(string.rindex('a'))
#
# print(string.count('a'))

# string = "wo shi xie wo ai zhonghua"
'''
替换字符串
replace(old, new[, count])
old 需要替换的原字符串
new 新字符串
count 替换个数，不写默认全部
返回值: 返回替换后的新字符串
注意:原来的字符串不会改变
'''
# print(string.replace("wo", "ni", 1))
# print(string)

'''
字符串首字母大写
capitalize()
返回值: 返回修改后的新字符串
注意:原来的字符串不会改变
'''
# print(string.capitalize())
# print(string)

'''
字符串每个单词首字母大写
title()
返回值: 返回修改后的新字符串
注意:原来的字符串不会改变
'''
# print(string.title())
# print(string)

# string = "Wo Shi xie wo ai Zhong-HuaKK"
'''
字符串每个字符小写
lower()
返回值: 返回修改后的新字符串
注意:原来的字符串不会改变
'''
# print(string.lower())
# print(string)

'''
字符串每个字符大写
upper()
返回值: 返回修改后的新字符串
注意:原来的字符串不会改变
'''
# print(string.upper())
# print(string)

# 字符串填充压缩
# string = "abc"
'''
根据指定的一个字符fillchar，将原有字符串填充到指定长度width
ljust(width, fillchar)
返回值: 返回填充后的字符串
注意: 原有字符串不会改变，只有原字符串长度 < 指定结果长度时才会填充
'''
# print(string.ljust(3, 'l'))
# print(string)

'''
根据指定的一个字符fillchar，将原有字符串向左填充到指定长度width（字符串前面）
rjust(width, fillchar)
返回值: 返回填充后的字符串
注意: 原有字符串不会改变，只有原字符串长度 < 指定结果长度时才会填充
'''
# print(string.rjust(10, 'l'))
# print(string)

'''
根据指定的一个字符fillchar，将原有字符串两边填充到指定长度width（字符串在中间）
center(width, fillchar)
返回值: 返回填充后的字符串
注意: 原有字符串不会改变，只有原字符串长度 < 指定结果长度时才会填充
'''
# print(string.center(10, 'l'))
# print(string)


# string = "wwoo shi ming  "
'''
移除原有字符串指定字符(默认为空白字符)
仅仅移除左侧
lstrip(chars)
参数：需要移除的字符集,移除'a'|'b'|'c'...
返回值: 返回移除后的字符串
注意: 原有字符串不会改变
'''
# print("|" + string.lstrip() + "|")
# print("|" + string.lstrip("wo") + "|")
# print("|" + string + "|")

# string = "  wwoo shi ming  wwoo"
'''
移除原有字符串指定字符(默认为空白字符)
仅仅移除左侧
rstrip(chars)
参数：需要移除的字符集,移除'a'|'b'|'c'...
返回值: 返回移除后的字符串
注意: 原有字符串不会改变
'''
# print("|" + string.rstrip() + "|")
# print("|" + string.rstrip("wo") + "|")
# print("|" + string + "|")


# string = "sa-18-20001229-19031404-0766-6113620"
# 字符串的分隔拼接
'''
将一个大的字符串分隔成几个子字符串
split(sep, maxsplit)
参数一：sep 分隔符
参数二： maxsplit 分隔次数，可以省略，有多少分隔多少
返回值：返回分隔后的字符串，组成为列表(list)
注意：不会改变原字符串
'''
# result = string.split("-", 4)
# print(result)
# print(string)

'''
根据指定的分隔符，返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
partition(sep)
参数一：sep 分隔符
返回值：
    如果找到分隔符，返回(分隔符左侧内容, 分隔符, 分隔符右侧内容) tuple类型
    如果没有找到分隔符，返回(原字符串, "", "") tuple类型
注意：不会改变原字符串,从左侧开始找分隔符
'''
# result = string.partition("|")
# print(result)
# print(string)

'''
根据指定的分隔符，返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
rpartition(sep)
参数一：sep 分隔符
返回值：
    如果找到分隔符，返回(分隔符左侧内容, 分隔符, 分隔符右侧内容) tuple类型
    如果没有找到分隔符，返回("", "", 原字符串) tuple类型
注意：不会改变原字符串,从右侧开始找分隔符
'''
# result = string.rpartition("-")
# print(result)
# print(string)

# string = "wo \n shi \r xie"
'''
按照换行符(\r,\n),将字符串拆成多个元素，保存到列表中
splitlines(keepends)
参数一：keepends 是否保留换行符 bool类型
返回值：
    被换行符分隔的多个字符串，作为元素组成的列表
    list类型
注意：不会改变原字符串
'''
# result = string.splitlines(True)
# print(result)
# print(string)


'''
根据指定字符串，将给定的可迭代对象，进行拼接，得到拼接后的拼接字符串
join(iterable)
参数一：iterable
        可迭代对象
        字符串
        元祖
        列表
        ...
        
返回值：拼接好的新字符串
'''
# items = ["sz", "18", "gg"]
# result = "-".join(items)
# print(result)


# 字符串函数判定操作
# name = "SZ"
'''
字符串中是否所有的字符都是字母
    不包含该数字，特殊符号，标点符号等等
    至少有一个字符
语法：isalpha()
返回值：是否全部是字母，bool类型
'''
# print(name.isalpha())

# string = "55 "
'''
字符串中是否所有的字符都是数字
    不包含该字母，特殊符号，标点符号等等
    至少有一个字符
语法：isdigit()
返回值：是否全部是数字，bool类型
'''
# print(string.isdigit())

# string = 'hh5 5'
'''
字符串中是否所有的字符都是数字或字母
    不包含该特殊符号，标点符号等等
    至少有一个字符
语法：isalnum()
返回值：是否全部是字母或数字，bool类型
'''
# print(string.isalnum())

# string = "\t \n\r"
'''
字符串中是否所有的字符都是空白符
    包含空格，缩进，换行等不可见转义符
    至少有一个字符
语法：isspace()
返回值：是否全部是空白符，bool类型
'''
# print(string.isspace())

# string = "2021-12-26: 某某报告.xls"
'''
判断一个字符串是否以某个前缀开头
语法：startswith(prefix, start=0, end=len(str))
参数一：prefix  需要判断的前缀字符串
参数二：start  判定的起始位置
参数三：end  判定的终止位置
返回值：是否以指定前缀开头
      bool  类型
'''
# print(string.startswith("21", 2, 4))

string = "2021-12-26: 某某报告.xls"
'''
判断一个字符串是否以某个后缀结尾
语法：endswith(suffix, start=0, end=len(str))
参数一：suffix  需要判断的后缀字符串
参数二：start  判定的起始位置
参数三：end  判定的终止位置
返回值：是否以指定前缀开头 
      bool  类型
'''
# print(string.endswith(".doc"))

# in 判断一个字符串，是否被另一个字符串包含
# not in 判断一个字符串，是否不被另一个字符串包含
print("wo" in "who am wo")
print("wo" not in "who am wo")