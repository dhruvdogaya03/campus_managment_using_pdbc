from database.connection import Database


class SkillDao:

    def addskill(self, skill):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = """
        INSERT INTO skills
        (skill_name, category)
        VALUES (%s, %s)
        """

        data = (
            skill.skill_name,
            skill.category
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

        return "Skill Added Successfully!"

    def getallskills(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = "SELECT * FROM skills"

        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result