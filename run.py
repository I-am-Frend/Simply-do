# Simple To-do list
# Made by Frend

# Task Input
def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"description": task, "complete": False})
    print("Task added successfully!")


# Mark the task as complete
def mark_task_complete(tasks):
    print("Tasks:")
    view_tasks(tasks)
    index = int(input("Enter the index of the task to mark as complete: "))
    if 0 <= index < len(tasks):
        tasks[index]["complete"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


# Task Viewer
def view_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"{i}. {task['description']} - {status}")


# Main
def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        mark_task_complete(tasks)
    elif choice == "3":
        view_tasks(tasks)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

