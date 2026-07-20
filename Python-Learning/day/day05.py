import json

name = input("请输入姓名")
age = int(input("请输入年龄"))

people = {
    "姓名" : name,
    "年龄" : age
}
with open("student.json","w",encoding = "utf-8") as f:
    json.dump(people,f,ensure_ascii=False)

with open("student.json","r",encoding = "utf-8") as f:
    student = json.load(f)
print(f"欢迎回来 {student['姓名']}")
print(f"你的年龄是{student['年龄']}")