class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = 'Pending'
        print(f"Task '{task}' added.")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            print(f"Task '{task}' updated to {status}.")
        else:
            print(f"Task '{task}' not found.")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for task, status in self.tasks.items():
                print(f"{task}: {status}")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to update: ")
            status = input("Enter the new status (Pending/Completed): ")
            todo_list.update_task(task, status)
        elif choice == '3':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
