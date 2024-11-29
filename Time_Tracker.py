import uuid
from datetime import datetime

class Task:
    def __init__(self, name, description, project_association):
        self.name = name
        self._task_id = str(uuid.uuid4())
        self.description = description
        self.status = False
        self.start_t = datetime.now()
        self.end_t = None
        self.duration = None
        self.prj_association = project_association

    @property
    def task_id(self):
        return self._task_id
    
    def mark_done(self):
        self.end_t = datetime.now()
        self.status = True

    def task_duration(self):
        if self.start_t and self.end_t:
            self._duration = (self.end_t - self.start_t).total_seconds() / 3600
        return self.duration
    
    def __str__(self):
        status = "Done" if self.status else "Not Done"
        return (f"Task ID: {self.task_id}, Name: {self.name}, Status: {status}, "
                f"Start: {self.start_t}, End: {self.end_t}")


class Projects:
    def __init__(self, name):
        self._name = name
        self.tasks = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("Project name cannot be empty.")

    def __str__(self):
        return f"Project: {self.name}, Number of Tasks: {len(self.tasks)}"

    def add_task(self, task):
        if task.task_id not in self.tasks:
            self.tasks[task.task_id] = task
        else:
            raise ValueError("Task with this ID already exists in the project.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("Task ID not found")

    def all_tasks(self):
        return list(self.tasks.values())
    

class TimeTracker:
    def __init__(self):
        self.projects = {}

    def add_project(self, project_name):
        if project_name not in self.projects:
            self.projects[project_name] = Projects(project_name)
        else:
            raise ValueError("Project with this name already exists.")

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

