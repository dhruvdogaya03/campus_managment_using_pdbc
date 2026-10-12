class Project:

    def __init__(
        self,
        project_id,
        project_name,
        description,
        skill_id,
        created_by):

        self.project_id = project_id
        self.project_name = project_name
        self.description = description
        self.skill_id = skill_id
        self.created_by = created_by