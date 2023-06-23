# Simple To-do list
# Made by Frend

# Task Input
def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"description": task, "complete": False})
    print("Task added successfully!")