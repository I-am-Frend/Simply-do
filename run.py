"""
Simple To-do list
"""
from simple_term_menu import TerminalMenu
from blessed import Terminal

# Made by Frend

# Task Input
def add_task(tasks):
    """
    Adds tasks to an list
    """
    task = input("Enter task description: ")
    tasks.append({"description": task, "complete": False})
    print("Task added successfully!")


# Mark the task as complete
def mark_task_complete(tasks):
    """
    Marks the selected task as complete on the list.
    """
    print("Tasks:")
    view_tasks(tasks)
    index = int(input("Enter the index of the task to mark as complete:\n "))
    if 0 <= index < len(tasks):
        tasks[index]["complete"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


# Task Viewer
def view_tasks(tasks):
    """
    Function to check if the task in question is complete or not.
    """
    for i, task in enumerate(tasks):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"{i}. {task['description']} - {status}")


# Edit Tasks
def edit_task(tasks):
    """
    A way to Edit tasks if a spelling error occurred, 
    or the task it self has changed.
    """
    print("Tasks:")
    choice_made = False
    while not choice_made:
        view_tasks(tasks)
        index = input("Enter the index of the task to edit:\n")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tasks):
                task = tasks[index]
                new_description = input("Enter new task description:\n")
                task["description"] = new_description
                print("Task edited successfully!")
                choice_made = True
            else:
                print("Invalid task index.")
        else:
            print("Invalid task index. Should be an integer.\n")


# Delete Tasks
def delete_task(tasks):
    """
    A function to Delete tasks if they are not needed
    """
    print("Tasks:")
    choice_made = False
    while not choice_made:
        view_tasks(tasks)
        index = input("Enter the index of the task to delete:\n")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task deleted successfully!")
                choice_made = True
            else:
                print("Invalid task index.")
        else:
            print("Invalid task index. Should be an integer.\n")

# Main
def main():
    """
    Runs all functions and a simple menu
    """
    tasks = []
    options = {
        "1": add_task,
        "2": mark_task_complete,
        "3": view_tasks,
        "4": edit_task,
        "5": delete_task,
        "6": lambda _: print("Exiting...")
    }

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit\n")

        choice = input("Enter your choice (1-6):\n")
        action = options.get(choice)
        if action:
            action(tasks)
        else:
            print("Invalid choice. Please try again.")
            continue

        if choice == "6":
            break


if __name__ == "__main__":
    main()
