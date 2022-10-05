# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 20:10:50

person = {"name": "zhangsan", "age": 12}

'''
str1 = "xbx, 18, 175"
l = str1.split(",")
print(l)

person = {"name": "zhangsan", "age": 12}
print(person, type(person))
print(person["name"])
print(person["age"])

d = dict.fromkeys("abc", 666)
print(d)
d1 = person.fromkeys("abc", 666)
print(d1)
d2 = person.fromkeys([1, 2, 3], 666)
print(d2)
d3 = person.fromkeys((1, 2, 3), 666)
print(d3)
'''

# p = {"kkk": person, "kkk": 123}
# print(p, type(p))
# d = {[1, 2, 3] : 13}
# print(d, type(d))

# 字典常规操作
# 添加一个键值对 dic[key] = value
# d = {"name": "admin", "age": 18}
# print(d, type(d), id(d))
# d["height"] = 180
# print(d, type(d), id(d))

# 删除操作
# 删除一个键值对 del dic[key],当删除的key不存在时，报错
# d = {"name": "admin", "age": 18}
# print(d, type(d), id(d))
# del d["name"]
# print(d, type(d), id(d))
# del d["ll"]

'''
dic.pop(key[, default])
删除指定的键值对，并返回对应的值
如果key不存在，返回给的的default值，如果没有指定default值，会报错
'''
# d = {"name": "admin", "age": 18}
# v = d.pop("age")
# v = d.pop("age1", 666)
# print(d, v)

'''
dic.popitem()
删除按升序排序后的第一个键值对，并以元组的形式返回键值对
如果字典为空，则报错
'''
# d = {"name": "admin", "age": 18}
# 返回元组
# dp = d.popitem()
# print(d, dp)
#
# d1 = {}
# dp1 = d1.popitem()
# print(d1, dp1)

'''
dic.clear()
删除字典内所有键值对
返回值：None
注意：字典对象本身还存在，只是清空了内容
del是删除一个键值对或整个字典
'''
# clear = d.clear()
# print(d, clear)
#
# del d
# print(d)

# 修改字典：只能修改值，不能修改键
'''
修改单个键值对
dic[key] = value
key不存在就是新增操作，存在就是修改操作
'''
# dic = {"name": "admin", "age": 18}
# dic["age"] = 20
# print(dic)

'''
批量修改键值对
oldDic.update(newDic) 返回值：None
根据新的字典，批量修改旧字典的键值对值
如果旧字典没有key，就新增该key
'''
# oldDic = {"name": "admin", "age": 18}
# newDic = {"name": "root", "height": 180}
# update = oldDic.update(newDic)
# print(oldDic, newDic, update)


# 字典查询操作
'''
查询单个键值对 
方式一： dic[key],key不存在报错
方式二： dic.get(key[, default]), key不存在会返回default值，如果没有给定default值，会返回None，但是原字典不会新增该键值对
方式二： dic.setdefault(key[, default]), key不存在会返回default值，如果没有给定default值，会返回None，原字典会新增该键值对
'''
# dic = {"name": "admin", "age": 18}
# print(dic["age"])

# dic_get = dic.get("name1")
# dic_get = dic.get("name1", "root")
# print(dic_get, dic)

# dic_setdefault = dic.setdefault("name1", "root")
# dic_setdefault = dic.setdefault("name1")
# print(dic_setdefault, dic)

'''
获取字典所有的值： dic.values()
获取字典所有的键： dic.keys()
获取字典所有的键值对： dic.items()
python2.x与python3.x之间获取键、值、键值对之间区别
1.python2.x获取到的直接是一个列表，可以通过下标进行获取指定元素
2.python3.x获取到的是Dictionary view objects改变键值对，获取到也跟着发生变化
3.python2.x提供如下方法:
viewkeys()
viewvalues()
viewitems()
作用如同.python3.x的Dictionary view objects
'''
# dic = {"name": "admin", "age": 18, "height": 666}
# vs = dic.values()
#
# ks = dic.keys()
#
# its = dic.items()
#
# print(ks, vs, its)
#
# dic["address"] = "shanghai"
# print(dic)
# print(ks, vs, its)

# 遍历所有的key，根据key获取所有的值
# dic = {"name": "admin", "age": 18, "height": 666}
# keys = dic.keys()
# for key in keys:
#     print(key)
#     print(dic[key])
# # 直接遍历所有的键值对
# items = dic.items()
# dic["address"] = "shanghai"
# print(items)
# for k, v in items:
#     print(k, v)


dic = {"name": "admin", "age": 18, "height": 666, "gg": person}
print(dic)
# 计算键值对个数
print(len(dic))


# 判定
# x in dic判定dic中的key是否存在x
# x not in dic判定dic中的key是否不存在x
# dic.has_key(key) 判定dic是否存在key，python2.x可以使用，但是过期了，使用in代替
print("name1" in dic)
print("name1" not in dic)
