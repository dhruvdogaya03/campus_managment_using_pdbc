from database.connection import Database


class ProjectMemberDao:

    def joinproject(self, member):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        INSERT INTO project_members
        (project_id, student_id, role, joined_date)
        VALUES (%s, %s, %s, CURDATE())
        """

        data = (
            member.project_id,
            member.student_id,
            member.role
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

        return "Student Joined Project Successfully!"

    def getprojectmembers(self, project_id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        SELECT
            s.student_id,
            s.name,
            s.branch,
            pm.role,
            pm.joined_date
        FROM project_members pm
        JOIN students s
            ON pm.student_id = s.student_id
        WHERE pm.project_id = %s
        """

        cursor.execute(query, (project_id,))

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result