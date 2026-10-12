from dao.project_dao import ProjectDao
from model.project import Project


class ProjectService:

    def addproject(self):

        project_name = input("Enter Project Name: ")

        description = input(
            "Enter Project Description: "
        )

        skill_id = int(
            input("Enter Required Skill ID: ")
        )

        created_by = int(
            input("Enter Creator Student ID: ")
        )

        p = Project(
            None,
            project_name,
            description,
            skill_id,
            created_by
        )

        db = ProjectDao()

        return db.addproject(p)

    def getallprojects(self):

        db = ProjectDao()

        return db.getallprojects()