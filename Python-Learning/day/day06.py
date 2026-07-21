import json


class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"姓名:{self.name}")
        print(f"年龄:{self.age}")

    def change(self,name,age):
        self.name = name
        self.age = age

    def to_dict(self):
        return{
            "姓名" : self.name,
            "年龄" : self.age
        }

student1 = Student("张三",20)

student1.change("李四",21)
student1.show()
data = student1.to_dict()
with open("student.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False)
