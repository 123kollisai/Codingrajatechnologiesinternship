class Task:
    def __init__(self, title, priority, due_date, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Title: {self.title}\nPriority: {self.priority}\nDue Date: {self.due_date}\nCompleted: {self.completed}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.mark_completed()

    def list_tasks(self):
        return self.tasks

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
def main():
    task_manager = TaskManager()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): choose any of the one ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, priority, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            title = input("Enter task title to remove: ")
            task = task_manager.get_task_by_title(title)
            if task:
                task_manager.remove_task(task)
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            task = task_manager.get_task_by_title(title)
            if task:
                task_manager.mark_task_completed(task)
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            tasks = task_manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"Task {index}:\n{task}\n")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import json

def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as file:
        task_list = [vars(task) for task in tasks]
        json.dump(task_list, file)

def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            task_list = json.load(file)
            tasks = [Task(**task) for task in task_list]
            return tasks
    except FileNotFoundError:
        return []

def main():
    task_manager = TaskManager()

    # Load tasks from file at the start of the application
    task_manager.tasks = load_tasks_from_file("tasks.json")

    while True:
        # ... (Rest of the code remains the same)

        # Save tasks to file whenever changes are made
        save_tasks_to_file(task_manager.list_tasks(), "tasks.json")
