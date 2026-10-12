from dao.skill_dao import SkillDao
from model.skill import Skill


class SkillService:

    def addskill(self):

        skill_name = input("Enter Skill Name: ")
        category = input("Enter Category: ")

        s = Skill(
            None,
            skill_name,
            category
        )

        db = SkillDao()

        return db.addskill(s)

    def getallskills(self):

        db = SkillDao()

        return db.getallskills()