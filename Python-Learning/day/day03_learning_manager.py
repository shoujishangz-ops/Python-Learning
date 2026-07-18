plans = [
    "Python",
    "Git",
    "RAG"
]
def show_plan(plans):
    print("当前的学习计划:")
    for plan in plans:
        print(plan)

def add_plan(plans):
    new_plan = input("请输入要添加的学习内容:")
    plans.append(new_plan)
    print("学习内容已添加")

def delete_plan(plans):
    del_plan = input("请输入要删除的学习内容:")
    if del_plan in plans:
        plans.remove(del_plan)
        print("删除成功")
    else:
        print("学习内容不存在")

def main():
    while True:
        print("AI学习计划管理器")
        print("1.查看学习计划")
        print("2.添加学习计划")
        print("3.删除学习计划")
        print("4.退出")
        choice = input("请输入操作编号:")
        if choice == "1":
            show_plan(plans)
        elif choice == "2":
            add_plan(plans)
        elif choice == "3":
            delete_plan(plans)
        elif choice == "4":
            print("成功退出程序")
            break
        else:
            print("输入编号有误，请重新输入")


if __name__ == "__main__":
    main()

main()