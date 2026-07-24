from models import Student
from services import StudentManager
from utils import to_json
from utils import from_json


def main():
    manager = StudentManager()
    
    while True:
        print("-----学生管理系统-----")
        print("1.添加学生")
        print("2.查看学生")
        print("3.删除学生")
        print("4.修改成绩")
        print("5.退出操作系统")
        while True:
            try:
                num = int(input("请输入操作编号:"))
                break
            except ValueError:
                print("请输入数字")
        if num == 1:
            id = int(input("请输入学生id:"))
            name = input("请输入学生名字:")
            score = float(input("请输入学生分数:"))
            new_student = Student(id,name,score)
            manager.add_student(new_student)
            print("添加成功！")
        elif num == 2:
            print(manager.show_students())
        elif num == 3:
            id = int(input("请输入要删除的学生id:"))
            student = manager.search_student(id)
            if student:
                print("已找到该学生")
                manager.delete_student(student)
                print("删除成功")
            else:
                print("未找到该学生")
        elif num == 4:
            id = int(input("请输入要删除的学生id:"))
            student = manager.search_student(id)
            if student:
                print("已找到该学生")
                score = float(input("请输入更改后的分数:"))
                manager.update_score(student,score)
            else:
                print("未找到该学生")
        elif num == 5:
            print("退出成功")
            break
        else:
            print("编号输入无效，请重新输入")

if __name__ =="__main__":
    main()