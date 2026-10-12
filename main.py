from service.student_service import StudentService
from service.skill_service import SkillService
from service.project_service import ProjectService
from service.project_member_service import ProjectMemberService


while True:

    print("\n======================================")
    print("      CAMPUS SKILL & PROJECT HUB")
    print("======================================")

    print("1. Student Management")
    print("2. Skill Management")
    print("3. Project Management")
    print("4. Join Project")
    print("5. View Project Members")
    print("6. Find Students by Skill")
    print("7. Student Dashboard")
    print("8. Project Dashboard")
    print("9. Exit")

    choice = int(input("Enter the choice: "))

    match choice:

        # ---------------- STUDENT ----------------

        case 1:

            while True:

                print("\n------ STUDENT MANAGEMENT ------")

                print("1. Add Student")
                print("2. View All Students")
                print("3. Delete Student")
                print("4. Back")

                ch = int(input("Enter choice: "))

                match ch:

                    case 1:

                        stu = StudentService()

                        result = stu.addstudent()

                        print(result)

                    case 2:

                        stu = StudentService()

                        result = stu.getallstudents()

                        print("\nID\tName\tEmail\tBranch\tYear")
                        print("------------------------------------------")

                        for row in result:

                            print(
                                row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                                sep="\t"
                            )

                    case 3:

                        stu = StudentService()

                        result = stu.deletestudent()

                        print(result)

                    case 4:

                        break

                    case _:

                        print("Invalid Choice!")

        # ---------------- SKILL ----------------

        case 2:

            while True:

                print("\n------ SKILL MANAGEMENT ------")

                print("1. Add Skill")
                print("2. View Skills")
                print("3. Back")

                ch = int(input("Enter choice: "))

                match ch:

                    case 1:

                        skill = SkillService()

                        result = skill.addskill()

                        print(result)

                    case 2:

                        skill = SkillService()

                        result = skill.getallskills()

                        print("\nID\tSkill\tCategory")
                        print("--------------------------------")

                        for row in result:

                            print(
                                row[0],
                                row[1],
                                row[2],
                                sep="\t"
                            )

                    case 3:

                        break

                    case _:

                        print("Invalid Choice!")

        # ---------------- PROJECT ----------------

        case 3:

            while True:

                print("\n------ PROJECT MANAGEMENT ------")

                print("1. Create Project")
                print("2. View All Projects")
                print("3. Back")

                ch = int(input("Enter choice: "))

                match ch:

                    case 1:

                        project = ProjectService()

                        result = project.addproject()

                        print(result)

                    case 2:

                        project = ProjectService()

                        result = project.getallprojects()

                        print(
                            "\nID\tProject\tDescription\tSkill\tCreated By"
                        )

                        print("------------------------------------------")

                        for row in result:

                            print(
                                row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                                sep="\t"
                            )

                    case 3:

                        break

                    case _:

                        print("Invalid Choice!")

        # ---------------- JOIN PROJECT ----------------

        case 4:

            member = ProjectMemberService()

            result = member.joinproject()

            print(result)

        # ---------------- VIEW MEMBERS ----------------

        case 5:

            member = ProjectMemberService()

            result = member.getprojectmembers()

            print("\nID\tName\tBranch\tRole\tJoined Date")
            print("------------------------------------------")

            for row in result:

                print(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    sep="\t"
                )

        # ---------------- FUTURE FEATURES ----------------

        case 6:

            print("\nI am willing To learn web  Development")

        case 7:
            print("\nI am willing To learn web  Development")
            print("\nFeature coming next: Student Dashboard")

        case 8:
            print("\nI am willing To learn web  Development")
            print("\nFeature coming next: Project Dashboard")

        # ---------------- EXIT ----------------

        case 9:
            print("\nI am willing To learn web  Development")
            print("\nThank you for using Campus Skill & Project Hub!")
            break

        case _:

            print("\nInvalid Choice!")