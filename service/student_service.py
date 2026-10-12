from dao.student_dao import StudentDao
from model.student import Student


class StudentService:

    def addstudent(self):

        name = input("Enter Student Name: ")
        email = input("Enter Email: ")
        branch = input("Enter Branch: ")
        year = int(input("Enter Year: "))

        s = Student(
            None,
            name,
            email,
            branch,
            year
        )

        db = StudentDao()

        return db.addstudent(s)

    def getallstudents(self):

        db = StudentDao()

        students = db.getallstudents()

        return students

    def deletestudent(self):

        student_id = int(input("Enter Student ID: "))

        db = StudentDao()

        return db.deletestudent(student_id)