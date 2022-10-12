# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022-10-11 21:07:42

class User(object):

    def add_user(self):
        print("添加用户")

    def delete_user(self):
        print("删除用户")

    def update_user(self):
        print("更新用户")

    def select_user(self):
        print("查找用户")

    def before_process(self, method):
        if method == "add":
            self.add_user()
        elif method == "delete":
            self.delete_user()
        elif method == "update":
            self.update_user()
        elif method == "select":
            self.select_user()
        else:
            print("无效调用")

    def after_process(self, method):
        """
        去除ifelse的繁琐，类似理由转发
        """
        # p判断是否存在该方法
        if hasattr(self, method):
            # 获取方法
            user_method = getattr(self, method)
            user_method()
        else:
            print("无效调用")


if __name__ == "__main__":
    # 没有处理，好多if
    User().before_process("delete")
    # 处理后
    User().after_process("delete_user")
