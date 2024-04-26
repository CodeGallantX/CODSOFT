class Task:
    def __init__(self, description, due_date, status="Pending"):
        self.description = description
        self.due_date = due_date
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                break
        else:
            print("Task not found.")

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.description} (Due: {task.due_date}, Status: {task.status})")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            todo_list.view_tasks()
            task_description = input("\nEnter task description to remove: ")
            todo_list.remove_task(task_description)
            print("Task removed successfully!")
        elif choice == "3":
            print("\nTASKS:")
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
