import json
from models import Student
from utils.logger import logger

def to_json(students: list[Student]) -> None:

    data = []
    for student in students:
        data.append(student.to_dict())

    with open("data/students.json","w",encoding ="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent = 4)

def from_json() -> list[Student]:

    try:
        with open(
            "data/students.json",
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


    except FileNotFoundError:

        logger.warning(
            "学生数据文件不存在，创建空数据"
        )
        return []

    except json.JSONDecodeError:

        logger.exception(
            "学生数据JSON格式错误，创建空数据"
        )
        return []


    students=[]

    for item in data:
        student=Student.from_dict(item)
        students.append(student)

    return students

          
