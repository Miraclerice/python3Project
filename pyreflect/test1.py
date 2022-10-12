# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022-10-11 20:28:36

# __import__()
# getattr()
# setattr()
# delattr()
# hasattr()

# 保证按位置传参且只能传一个
def new_method(self, /):
    print("我是新来的，给我一个实例")


def main():
    """
    动态加载模块，创建类实例执行其中方法
    """
    # 动态导入模块Func
    func_module = __import__("Func", fromlist=True)
    print(func_module)

    # 判断是否找到对应类
    if hasattr(func_module, "Func"):
        # 通过模块对象实例获取类对象实例
        func_class = getattr(func_module, "Func")
        # print(type(func_class))
        print(func_class)

        # 判断是否存在方法
        if hasattr(func_class, "process"):
            # 通过类对象获取成员方法
            process_method = getattr(func_class, "process")
            # print(type(process_method))
            print(process_method)
            # 执行该方法
            process_method(func_class)
        else:
            print("没有找到当前方法")

        # 向类添加方法
        setattr(func_class, "newFunc", new_method)
        # 是否成功添加方法
        if hasattr(func_class, "newFunc"):
            # 获取该方法
            new_func = getattr(func_class, "newFunc")
            # 执行方法
            new_func(func_class)
        else:
            print("添加失败")

        # 删除Func类中法
        delattr(func_class, "newFunc")
        if not hasattr(func_class, "newFunc"):
            print("删除成功")
    else:
        print("没有找到该类")


# 测试代码
if __name__ == "__main__":
    main()
