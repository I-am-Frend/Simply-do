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