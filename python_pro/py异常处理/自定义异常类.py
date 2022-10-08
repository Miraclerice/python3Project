# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/7/0007 0:01:32


class MyException(Exception):
    def __init__(self, msg, error_code=200):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return self.msg + ":" + str(self.error_code)

def setAge(age):
    if age <= 0 or age > 200:
        raise MyException("年龄不符合，值错误", 404)
    else:
        print(age)


try:
    setAge(-2)
except MyException as e:
    print(e)
