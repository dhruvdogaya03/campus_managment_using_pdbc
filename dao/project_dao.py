from database.connection import Database


class ProjectDao:

    def addproject(self, project):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        INSERT INTO projects
        (project_name, description, skill_id, created_by)
        VALUES (%s, %s, %s, %s)
        """

        data = (
            project.project_name,
            project.description,
            project.skill_id,
            project.created_by
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

        return "Project Created Successfully!"

    def getallprojects(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        SELECT
            p.project_id,
            p.project_name,
            p.description,
            s.skill_name,
            st.name
        FROM projects p
        JOIN skills s
            ON p.skill_id = s.skill_id
        JOIN students st
            ON p.created_by = st.student_id
        """

        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result