import json

def print_documents(documents):
    for i,document in enumerate(documents,start=1):
        print(f"学生{i}:")
        for key,value in document.items():
            print(f"{key}:{value}")
        print()

def store_data(students):
    try:
        with open("student.json","w",encoding="utf-8") as f:
            json.dump(students,f,ensure_ascii=False)
    except Exception:
        print("保存失败")

def show_students():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

    return students

def add_student(students):
    name = input("请输入学生姓名:")

    while True:
        try:
            age = int(input("请输入年龄:"))
            break
        except ValueError:
            print("年龄输入有误，请输入整数")

    student ={
        "姓名" : name,
        "年龄" : age
    }

    students.append(student)

def change_student(students):
    while True:
        try:
            num = int(input("修改第几个学生:"))
            if 1<= num <= len(students):
                    break
            else:
                    print("未找到该学生")
        except ValueError:
            print("请输入阿拉伯数字")
    name = input("请输入更改后的学生姓名")
    while True:
        try:
            age = int(input("请输入更改后的年龄:"))
            break
        except ValueError:
            print("年龄输入有误，请输入整数")
    students[num-1]["姓名"] = name
    students[num-1]["年龄"] = age
    print("更改成功")
    return students

def delete_student(students):
    while True:
        try:
            num = int(input("请输入要删除的学生编号"))
            if 1 <= num <=len(students):
                break
            else:
                print("没有这个学生")
        except ValueError:
                print("请输入阿拉伯数字")
    
    del students[num-1]
    print("删除成功")
    return students

    


def menu():
        print("—————————学生数据系统————————")
        print("1.添加学生")
        print("2.查看学生")
        print("3.修改学生")
        print("4.删除学生")
        print("5.退出")
        print()

def main():
    while True:
        students = show_students()
        menu()
        num = input("请输入操作编号:")
        if num == "1":
            add_student(students)
            store_data(students)
        elif num == "2":
            print_documents(students)
        elif num == "3":
            students = change_student(students)
            store_data(students)
        elif num =="4":
            students = delete_student(students)
            store_data(students)
        elif num =="5":
            print("退出程序中...")
            break
        else:
            print("编号输入错误")
    print("退出成功")

main()