import student_manager

def main():
    students = student_manager.load_students()
    while True:
        student_manager.menu()
        num = input("请输入操作编号:")
        if num == "1":
            student = student_manager.create_student()
            results =student_manager.add_student(students,student)
            print(results["message"])
            result =student_manager.store_data(students)
            if result["success"]:
                print("保存成功")
            else:
                print(result["message"])
        elif num == "2":
            student_manager.print_documents(students)
        elif num == "3":
            id = student_manager.get_student_id(students)
            results = student_manager.change_student(students,id)
            print(results["message"])
            result =student_manager.store_data(students)
            if result["success"]:
                print("保存成功")
            else:
                print(result["message"])
        elif num =="4":
            while True:
                id = student_manager.get_student_id(students)
                results = student_manager.delete_student(students,id)
                if results["success"]:
                    print(results["message"])
                    break
                else:
                    print(results["message"])
            result =student_manager.store_data(students)
            if result["success"]:
                print("保存成功")
            else:
                print(result["message"])

        elif num =="5":
            print("退出程序中...")
            break
        else:
            print("编号输入错误")
    print("退出成功")

if __name__ == "__main__":
    main()