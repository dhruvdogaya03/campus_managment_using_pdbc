from dao.project_member_dao import ProjectMemberDao
from model.project_member import ProjectMember


class ProjectMemberService:

    def joinproject(self):

        project_id = int(
            input("Enter Project ID: ")
        )

        student_id = int(
            input("Enter Student ID: ")
        )

        role = input("Enter Role: ")

        member = ProjectMember(
            None,
            project_id,
            student_id,
            role,
            None
        )

        db = ProjectMemberDao()

        return db.joinproject(member)

    def getprojectmembers(self):

        project_id = int(
            input("Enter Project ID: ")
        )

        db = ProjectMemberDao()

        return db.getprojectmembers(project_id)