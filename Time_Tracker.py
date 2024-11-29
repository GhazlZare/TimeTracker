from project import *

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
        print(f"Task created with ID: {new_task.task_id}")

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
    
