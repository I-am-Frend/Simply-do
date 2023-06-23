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
    options = {
        "1": add_task,
        "2": mark_task_complete,
        "3": view_tasks,
        "4": lambda _: print("Exiting...")
    }

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        action = options.get(choice)
        if action:
            action(tasks)
        else:
            print("Invalid choice. Please try again.")
            continue

        if choice == "4":
            break

if __name__ == "__main__":
    main()