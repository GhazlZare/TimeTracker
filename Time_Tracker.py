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
    
def main():
    tracker = TimeTracker()

    while True:
        print('''What do you want to do?
                1. Create project
                2. Create task
                3. Mark task done
                4. Add existing task to a project
                5. List tasks in a project
                6. Edit a task
                7. Delete task
                8. Display project details
                9. List all projects
                10. Search for a task
                11. Exit''')
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                project_name = input("Enter project name: ")
                tracker.create_project(project_name)
                print("Project created successfully.")
            elif choice == 2:
                project_name = input("Enter project name: ")
                task_name = input("Enter task name: ")
                description = input("Enter task description: ")
                tracker.create_task(project_name, task_name, description)
                print("Task created successfully.")
            elif choice == 3:
                project_name = input("Enter project name: ")
                task_id = input("Enter task ID: ")
                tracker.edit_task(project_name, task_id, status=True)
                print("Task marked as done.")
            elif choice == 4:
                project_name = input("Enter project name: ")
                task_id = input("Enter task ID of the existing task: ")

                found_task = None
                for proj in tracker.projects.values():
                    if task_id in proj.tasks:
                        found_task = proj.tasks[task_id]
                        break

                if found_task:
                    target_project = tracker.get_project(project_name)
                    target_project.add_task(found_task)
                    print("Task added to the project successfully.")
                else:
                    print("Task ID not found in any existing project.")
            elif choice == 5:
                project_name = input("Enter project name: ")
                tasks = tracker.list_tasks(project_name)
                print("\n".join(tasks) if tasks else "No tasks found.")
            elif choice == 6:
                project_name = input("Enter project name: ")
                task_id = input("Enter task ID: ")
                task_name = input("Enter new task name (leave blank to skip): ") or None
                description = input("Enter new description (leave blank to skip): ") or None
                status = input("Mark as done? (yes/no, leave blank to skip): ").lower()
                status = True if status == "yes" else None
                tracker.edit_task(project_name, task_id, task_name, description, status)
                print("Task edited successfully.")
            elif choice == 7:
                project_name = input("Enter project name: ")
                task_id = input("Enter task ID: ")
                tracker.delete_task(project_name, task_id)
                print("Task deleted successfully.")
            elif choice == 8:
                project_name = input("Enter project name: ")
                tracker.display_project_details(project_name)
            elif choice == 9:
                projects = tracker.list_projects()
                print("\n".join(projects) if projects else "No projects found.")
            elif choice == 10:
                term = input("Enter search term: ")
                matches = tracker.search_task(term)
                for task in matches:
                    print(task)
            elif choice == 11:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

main()