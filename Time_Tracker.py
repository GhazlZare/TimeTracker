import uuid
from datetime import datetime

class Task:
    def __init__(self, name, description, project_association):
        self._name = name
        self._task_idtask_id =str(uuid.uuid4())
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
        if self._start_t and self._end_t:
            self._duration = (self._end_t - self._start_t).total_seconds() / 3600
        return self._duration
    
    def __str__(self):
        status = "Done" if self.status else "Not Done"
        return (f"Task ID: {self.task_id}, Name: {self.name}, Status: {status}, "
                f"Start: {self.start_time}, End: {self.end_time}")


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
        self.tasks[task.task_id] = task

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