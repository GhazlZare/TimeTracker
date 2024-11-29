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
        if project_name in self.projects:
            del self.projects[project_name]
        else:
            raise ValueError("Project not found.")

    def get_project(self, project_name):
        if project_name in self.projects:
            return self.projects[project_name]
        else:
            raise ValueError("Project not found.")

    def list_projects(self):
        return list(self.projects.keys())

    def create_project(self, project_name):
        self.add_project(project_name)

    def create_task(self, project_name, name, description):
        project = self.get_project(project_name)
        new_task = Task(name, description, project_name)
        project.add_task(new_task)

    def edit_task(self, project_name, task_id, name=None, description=None, status=None):
        project = self.get_project(project_name)
        if task_id in project.tasks:
            task = project.tasks[task_id]
            if name is not None:
                task.name = name
            if description is not None:
                task.description = description
            if status is not None:
                task.status = status
                if status:  
                    task.mark_done()
        else:
            raise ValueError("Task ID not found in project.")

    def delete_task(self, project_name, task_id):
        project = self.get_project(project_name)
        project.remove_task(task_id)

    def list_tasks(self, project_name):
        project = self.get_project(project_name)
        return [str(task) for task in project.all_tasks()]

    def display_project_details(self, project_name):
        try:
            project = self.get_project(project_name)
            print(f"Project: {project.name}")
            print(f"Number of Tasks: {len(project.tasks)}")
            if project.tasks:
                print("\nTasks:")
                for task in project.all_tasks():
                    print(task)
            else:
                print("No tasks available in this project.")
        except ValueError as e:
            print(str(e))

    def search_task(self, search_term):
        matching_tasks = []
        for project in self.projects.values():
            for task in project.all_tasks():
                if search_term.lower() in task.name.lower() or search_term.lower() in task.description.lower():
                    matching_tasks.append(task)
        return matching_tasks

