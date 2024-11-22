import uuid
from datetime import datetime

class Task:
    def __init__(self, name, description, project_association):
        self.name = name
        self.task_id = uuid.uuid5
        self.description = description
        self.status = False
        self.start_t = datetime.now()
        self.end_t = None
        self.duration = None
        self.prj_association = project_association

    def mark_done(self):
        self.end_t = datetime.now()
        self.status = True

    def task_duration(self):
        pass


class Projects:
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self):
        self.tasks[task.task_id] = uuid.uuid4

    def remove_task(self, task_id):
        pass

    def all_tasks(self):
        return self.tasks.values
    

class TimeTracker:
    def __init__(self) -> None:
        self.pojects = {}

    def add_project(self, project_name):
        self.projects[project.name] = project_name

    def remove_project(self, project_name):
        pass

    def get_project(self, project_name):
        pass

    def list_projects(self):
        pass

    def create_project(time_tracker, project_name):
        pass

    def create_task(project, task_id, name, description):
        pass

    def edit_task(project, task_id, name=None, description=None, status=False, start_time=None, end_time=None):
        pass

    def delete_task(project, task_id):
        project.remove_task(task_id)

    def list_tasks(project):
        for task in project.list_tasks():
            pass