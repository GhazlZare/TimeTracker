from Time_Tracker import *

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

if __name__ == "__main__":
    main()