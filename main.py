tasks = []

tasks.append("Buy groceries")
tasks.append("Do Laundry")
tasks.append("Go for a run")

def add_task(task):
    tasks.append(task)

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def mark_task_completed(index):
    if index < len(tasks):
        print(f"Task ' {tasks[index]}' marked as completed")
    else:
        print("Invalid task index")

def remove_task(index):
    if index < len(tasks):
        print(f"Task '{tasks[index]}' removed.")
        tasks.pop(index)
    else:
        print("Invalid task index.")
        
while True:
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter task index: "))
        mark_task_completed(index)
    elif choice == "4":
        index = int(input("Enter task index: "))
        remove_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")