from task import *

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