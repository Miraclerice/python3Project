# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022-10-11 21:34:18
import os

filename = "./student.txt"
encoding = "utf-8"
choice_list = [0, 1, 2, 3, 4, 5, 6, 7]


class System:
    def main(self):
        while True:
            self.menu()
            choice = int(input("请输入您的选择\n"))
            if choice in choice_list:
                if choice == 0:
                    answer = input("你是否要退出?y/n\n")
                    if answer == "y" or answer == "Y":
                        print("谢谢您的使用")
                        exit()
                    else:
                        continue
                elif choice == 1:
                    self.insert()
                elif choice == 2:
                    self.search()
                elif choice == 3:
                    self.delete()
                elif choice == 4:
                    self.modify()
                elif choice == 5:
                    self.sort()
                elif choice == 6:
                    self.total()
                elif choice == 7:
                    self.show()

    def menu(self):
        print("-" * 20 + "学生管理系统" + "-" * 20)
        print("-" * 20 + " 功能菜单 " + "-" * 20)
        print("\t" * 5 + "1.录入学生信息")
        print("\t" * 5 + "2.查找学生信息")
        print("\t" * 5 + "3.删除学生信息")
        print("\t" * 5 + "4.修改学生信息")
        print("\t" * 5 + "5.排序")
        print("\t" * 5 + "6.统计学生总人数")
        print("\t" * 5 + "7.显示使用学生信息")
        print("\t" * 5 + "0.退出")
        print("-" * 50)

    def insert(self):
        student_list = []
        while True:
            sid = input("请输入您的id：\n")
            if not sid:
                break
            name = input("请输入您的姓名：\n")
            if not name:
                break
            try:
                english = int(input("请输入您的英语成绩：\n"))
                python = int(input("请输入您的python成绩：\n"))
                java = int(input("请输入您的java成绩：\n"))
            except ValueError:
                print("输入无效，不是整数类型，请您重新输入：\n")
                continue
            # 将学生信息保存到字典中
            student = {"id": sid, "name": name, "english": english, "python": python, "java": java}
            # 将学生字典添加到列表
            student_list.append(student)
            answer = input("是否继续添加?y/n\n")
            if answer == "y" or answer == "Y":
                continue
            else:
                break
        # 调用save函数
        self.save(student_list)
        print("学生录入完毕！")

    def save(self, stu_list):
        try:
            stu_txt = open(filename, "a", encoding=encoding)
        except Exception:
            stu_txt = open(filename, "w", encoding=encoding)
        for student in stu_list:
            stu_txt.write(str(student) + "\n")
        stu_txt.close()

    def show_student(self, stu_list):
        if len(stu_list) == 0:
            print("没有查到任何学生，无数据显示！！！")
            return
        # 定义标题
        format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t"
        print(format_title.format("id", "姓名", "英语成绩", "python成绩", "java成绩", "总成绩"))
        # 定义内容显示格式
        format_data = "{:^6}\t{:^14}\t{:^8}\t{:^8}\t{:^10}\t{:^8}\t"
        for stu in stu_list:
            print(format_data.format(stu["id"],
                                     stu["name"],
                                     stu["english"],
                                     stu["python"],
                                     stu["java"],
                                     int(stu.get("english")) + int(stu.get("python")) + int(stu.get("java"))
                                     ))

    def search(self):
        student_query = []
        while True:
            sid = ""
            name = ""
            if os.path.exists(filename):
                mode = input("按照id查找请输入1，按照姓名查找请输入2：\n")
                if mode == "1":
                    sid = input("请输入学生id：\n")
                elif mode == "2":
                    name = input("请您输入学生姓名：\n")
                else:
                    print("您输入有误，请您重新输入")
                    continue
                with open(filename, "r", encoding=encoding) as rfile:
                    students = rfile.readlines()
                    for stu in students:
                        d = dict(eval(stu))
                        if "" != sid:
                            if d["id"] == sid:
                                student_query.append(d)
                        elif "" != name:
                            if d["name"] == name:
                                student_query.append(d)
                # 显示查询结果
                self.show_student(student_query)
                # 清空列表
                student_query.clear()
                answer = input("是否继续查询？y/n\n")
                if answer == "y" or answer == "Y":
                    continue
                else:
                    break
            else:
                print("暂未保存学生信息 ")
                return

    def delete(self):
        while True:
            stu_id = input("请您输入学生id：\n")
            if "" != stu_id:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf=8") as rfile:
                        stu_old = rfile.readlines()
                else:
                    stu_old = []
                flag = False
                if stu_old:
                    with open(filename, "w", encoding="utf_8") as wfile:
                        d = {}
                        for stu in stu_old:
                            d = dict(eval(stu))
                            if d["id"] != stu_id:
                                wfile.write(str(d) + "\n")
                            else:
                                flag = True
                        if flag:
                            print(f"id为{stu_id}的学生已经被删除")
                        else:
                            print(f"没有找到id为{stu_id}的学生")
                else:
                    print("无任何学生信息")
                    break
                self.show()
                answer = input("是否继续删除?y/n\n")
                if answer == "y" or answer == "Y":
                    continue
                else:
                    break

    def modify(self):
        self.show()
        if os.path.exists(filename):
            with open(filename, "r", encoding=encoding) as rfile:
                stu_old = rfile.readlines()
        else:
            return
        stu_id = input("请您输入要修改的学生id:\n")
        with open(filename, "w", encoding=encoding) as wfile:
            for stu in stu_old:
                d = dict(eval(stu))
                if d["id"] == stu_id:
                    print("找到该学生信息了，可以进行修改")
                    while True:
                        try:
                            d["name"] = input("请输入学生姓名:\n")
                            d["english"] = int(input("请输入英语成绩:\n"))
                            d["python"] = int(input("请输入python成绩:\n"))
                            d["java"] = int(input("请输入java成绩:\n"))

                        except ValueError:
                            print("您输入的成绩不是整型，请您重新输入")
                            continue
                        else:
                            break
                    wfile.write(str(d) + "\n")
                    print("修改成功")
                else:
                    wfile.write(str(d) + "\n")
                    answer = input("是否继续修改其他学生信息?y/n\n")
                    if answer == "y" or answer == "Y":
                        continue
                    else:
                        break

    def sort(self):
        self.show()
        if not os.path.exists(filename):
            print("暂未存入学生信息")
            return
        with open(filename, "r", encoding=encoding) as rfile:
            student_list = rfile.readlines()
            student_new = []
        for stu in student_list:
            d = dict(eval(stu))
            student_new.append(d)
        asc_or_desc = input("请选择（0：升序，1：降序）\n")
        if asc_or_desc == '0':
            asc_or_desc_bool = False
        elif asc_or_desc == '1':
            asc_or_desc_bool = True
        else:
            print("您的输入有误，请重新输入")
            self.sort()
        mode = input("请选择排序方式（1.按英语成绩排序，2.按python成绩排序，3.按java成绩排序，0.按总成绩排序）:\n")
        if mode == "1":
            student_new.sort(key=lambda dic: int(dic["english"]), reverse=asc_or_desc_bool)
        elif mode == "2":
            student_new.sort(key=lambda dic: int(dic["python"]), reverse=asc_or_desc_bool)
        elif mode == "3":
            student_new.sort(key=lambda dic: int(dic["java"]), reverse=asc_or_desc_bool)
        elif mode == "0":
            student_new.sort(key=lambda dic: int(dic["english"]) + int(dic["python"]) + int(dic["java"]),
                             reverse=asc_or_desc_bool)
        else:
            print("您的输入有误请重新输入！！！")
            self.sort()
        self.show_student(student_new)

    def total(self):
        if not os.path.exists(filename):
            print("暂未存入学生信息....")
            return
        with open(filename, "r", encoding=encoding) as rfile:
            students = rfile.readlines()
        if students:
            print(f"一共有{len(students)}名学生")
        else:
            print("还没有录入学生信息")

    def show(self):
        stu_list = []
        if not os.path.exists(filename):
            print("暂未存入学生信息")
            return
        with open(filename, "r", encoding=encoding) as rfile:
            students = rfile.readlines()
        for student in students:
            stu_list.append(eval(student))
        if stu_list:
            self.show_student(stu_list)


if __name__ == "__main__":
    System().main()
