from models import Student
from utils import from_json,to_json
from utils.logger import logger

class StudentManager:

    def __init__(self):

        self.students: list[Student] = from_json()


    def add_student(self,student: Student) -> None:

        self.students.append(student)

        to_json(self.students)

        logger.info(
            f"添加学生成功 id={student.id}"
        )
    

    def delete_student(self,student: Student) -> None:

        self.students.remove(student)

        to_json(self.students)

        logger.info(
            f"删除学生成功 id={student.id}"
        )


    def search_student(self,id: int) -> Student | None:

        for student in self.students:
            if(student.id == id):
                return student

        logger.warning(
            f"未找到学生 id={id}"
        )
        return None


    def update_score(self,student: Student,score: float) -> None:

        student.score = score

        to_json(self.students)

    def show_students(self) -> list:

        if not self.students:
            return"暂无学生信息"

        result = []

        result.append("=====学生列表=====")
        result.append(
            f"{'ID':<10}{'姓名':<10}{'成绩':<10}{'创建时间':<20}"
        )
        result.append("-"*50)

        for student in self.students:
            result.append(
                f"{student.id:<10}"
                f"{student.name:<10}"
                f"{student.score:<10}"
                f"{student.create_at.strftime('%Y-%m-%d %H:%M')}"
            )
        result.append("-"*50)
        result.append(
            f"共{len(self.students)}名学生"
        )

        return "\n".join(result)


