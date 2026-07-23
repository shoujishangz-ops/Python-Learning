from models import Student
from utils import from_json
from utils import to_json

class StudentManager:

    def __init__(self):

        self.students: list[Student] = from_json()


    def add_student(self,student: Student) -> None:

        self.students.append(student)

        to_json(self.students)
    

    def delete_student(self,student: Student) -> None:

        self.students.remove(student)

        to_json(self.students)


    def search_student(self,id: int) -> Student|None:

        for student in self.students:
            if(student.id == id):
                return {
                    "success":True,
                    "manage":"查询到该学生",
                    "data":student
                }
        return {
                    "success":False,
                    "manage":"未查询到该学生",
                }


    def update_score(self,student: Student,score: float) -> None:

        student.score = score

        to_json(self.students)

    def show_students(self) -> list:

        if not self.students:
            return"暂无学生信息"

        result = []

        result.append("=====学生列表=====")
        result.append(
            f"{'ID':<10}{'姓名':<10}{'成绩':<10}"
        )
        result.append("-"*20)

        for student in self.students:
            result.append(
                f"{student.id:<10}{student.name:<10}{student.score:<10}"
            )
        result.append("-"*20)
        result.append(
            f"共{len(self.students)}名学生"
        )

        return "\n".join(result)


