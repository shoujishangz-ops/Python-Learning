import json


#数据操作

def store_data(students):
    try:
        with open("student.json","w",encoding="utf-8") as f:
            json.dump(students,f,ensure_ascii=False)
        return{
            "success" : True,
            "message" : "保存成功"
            }
    except Exception as e:
        return {
            "success":False,
            "message":"保存失败"+str(e)
        }

def load_students():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

    return students

#学生操作
def get_student_id(students):
    while True:
        try:
            num = int(input("请输入学生编号:"))

            if 1 <= num <= len(students):
                return num
            else:
                print("没有这个学生")

        except ValueError:
            print("请输入数字:")

def create_student():
    while True:  
        name = input("请输入学生姓名:")
        if name:
            break
        else:
            print("添加学生姓名不能为空")

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
    return student

def add_student(students,student):
    students.append(student)
    return {
        "success" : True,
        "message" : "添加成功",
        "data" : students
    }

def change_student(students,id):
    while True:
        name = input("请输入更改后的学生姓名")
        if name:
            break
    while True:
        try:
            age = int(input("请输入更改后的年龄:"))
            break
        except ValueError:
            print("年龄输入有误，请输入整数")
    students[id-1]["姓名"] = name
    students[id-1]["年龄"] = age
    return {
        "success" : True,
        "message" : "修改成功",
        "data" : students
    }

def delete_student(students,id):
    if not 1 <= id <=len(students):
        return{
            "success" : False,
            "message" : "未找到该学生",
            "data" : None
        }
    else: 
        del students[id-1]
        return {
            "success" : True,
            "message" : "删除成功",
            "data" : students
        }

    
#显示

def print_documents(documents):
    for i,document in enumerate(documents,start=1):
        print(f"学生{i}:")
        for key,value in document.items():
            print(f"{key}:{value}")
        print()

def menu():
        print("—————————学生数据系统————————")
        print("1.添加学生")
        print("2.查看学生")
        print("3.修改学生")
        print("4.删除学生")
        print("5.退出")
        print()

if __name__ == "__main__":
    print("管理工具加载中")
