"""
Simple To-do list
"""
from simple_term_menu import TerminalMenu
from blessed import Terminal

# Made by Frend
term = Terminal()

# Print Clear
def print_clear():
    """
    Clears the prints in the terminal
    """
    print(term.home + term.clear)

# Task Input
def add_task(tasks):
    """
    Adds tasks to an list
    """
    print_clear()
    task = input("Enter task description: ")
    tasks.append({"description": task, "complete": False})
    print(term.green + "Task added successfully!")

# Checks for empty tasks
def check_empty(tasks):
    """
    Checks for empty tasks
    """
    return len(tasks) > 0

# Mark the task as complete
def mark_task_complete(tasks):
    """
    Marks the selected task as complete on the list.
    """
    if check_empty(tasks):
        print_clear()       
        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input("Enter the index of the task to mark as complete:\n ")
            if index.isdigit():
                index = int(index)                
                if 0 <= index < len(tasks):
                    tasks[index]["complete"] = True
                    print_clear()
                    print(term.green + "Task marked as complete!")
                    choice_made = True
                else:
                    print_clear()

                    print(term.red + "Invalid task index.")
            elif index.lower() == 'q':
                choice_made = True
            else:
                print_clear()

                print(term.red + "Invalid task index. Should be an integer.\n")
    else:
        print_clear()
        print(term.red + "There are no tasks. Please add some.")


# Task Viewer
def view_tasks(tasks):
    """
    Function to check if the task in question is complete or not.
    """
    if check_empty(tasks):
        for i, task in enumerate(tasks):
            status = "Complete" if task["complete"] else "Incomplete"
            print(term.yellow + f"{i}. {task['description']} - {status}" + term.normal)
    else:
        print_clear()
        print(term.red + "There are no tasks" + term.normal)


# Edit Tasks
def edit_task(tasks):
    """
    A way to Edit tasks if a spelling error occurred, 
    or the task it self has changed.
    """
    if check_empty(tasks):
        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input("Enter the index of the task to edit:\n")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(tasks):
                    task = tasks[index]
                    new_description = input("Enter new task description:\n")
                    print_clear()
                    print(term.green + "Task edited successfully!" + term.normal)
                    choice_made = True
                else:
                    print_clear()
                    print(term.red + "Invalid task index." + term.normal)
            elif index.lower() == 'q':
                choice_made = True
            else:
                print_clear()
                print(term.red + "Invalid task index. Should be an integer.\n" + term.normal)
    else:
        print_clear()
        print(term.red + "There are no tasks. Please add some." + term.normal)


# Delete Tasks
def delete_task(tasks):
    """
    A function to Delete tasks if they are not needed
    """
    if check_empty(tasks):
        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input("Enter the index of the task to delete:\n")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(tasks):
                    del tasks[index]
                    print_clear()
                    print(term.green + "Task deleted successfully!" + term.normal)
                    choice_made = True
                else:
                    print_clear()
                    print(term.red + "Invalid task index." + term.normal)
            elif index.lower() == 'q':
                choice_made = True
            else:
                print_clear()
                print(term.red + "Invalid task index. Should be an integer.\n" + term.normal)
    else:
        print_clear()
        print(term.red + "There are no tasks. Please add some" + term.normal)

# Main
def main():
    """
    Runs all functions and a simple menu
    """
    tasks = []
    options = ["Add task", "Mark task Complete", "View task", "Edit task", "Delete task", "Exit"]

    menu = TerminalMenu(options, title="To-do manager")
    while True:
        print(term.normal)
        choice = menu.show()
        if choice != None:
            if options[choice] == "Add task":
                add_task(tasks)
            elif options[choice] == "Mark task complete":
                mark_task_complete(tasks)
            elif options[choice] == "View tasks":
                view_tasks(tasks)
            elif options[choice] == "Edit task":
                edit_task(tasks)
            elif options[choice] == "Delete task":
                delete_task(tasks)
            else:
                print("Exiting....")
                break
        else:
            choice = -1

        if choice == "6":
            break


if __name__ == "__main__":
    main()
