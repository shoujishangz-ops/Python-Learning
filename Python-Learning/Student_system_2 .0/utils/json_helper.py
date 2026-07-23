import json
from models import Student

def to_json(students: list[Student]) -> None:

    data = []
    for student in students:
        data.append(student.to_dict())

    with open("data/students.json","w",encoding ="utf-8") as f:
        json.dump(data,f,ensure_ascii=False)

def from_json() -> list[Student]:

    try:
        with open(
            "data/students.json",
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


    students=[]

    for item in data:
        student=Student.from_dict(item)
        students.append(student)

    return students

          
