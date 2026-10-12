from database.connection import Database


class StudentDao:

    def addstudent(self, student):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        INSERT INTO students
        (name, email, branch, year)
        VALUES (%s, %s, %s, %s)
        """

        data = (
            student.name,
            student.email,
            student.branch,
            student.year
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

        return "Student Added Successfully!"

    def getallstudents(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "SELECT * FROM students"

        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result

    def deletestudent(self, student_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        DELETE FROM students
        WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))

        conn.commit()

        cursor.close()
        conn.close()

        return "Student Deleted Successfully!"


    
