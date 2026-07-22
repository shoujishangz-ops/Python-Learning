from models import Student
from utils import from_json
from utils import to_json

class StudentManager:

    def __init__(self):

        self.students = from_json()


    def add_student(self,student):

        self.students.append(student)

        to_json(self.students)
    

    def delete_student(self,student):

        self.students.remove(student)

        to_json(self.students)


    def search_student(self,id):

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


    def update_score(self,student,score):

        student.score = score

        to_json(self.students)

    def show_students(self):
        return[
            student.to_dict()
            for student in self.students
        ]


