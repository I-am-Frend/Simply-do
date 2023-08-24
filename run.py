"""
Simple To-do list
"""
from simple_term_menu import TerminalMenu
from blessed import Terminal

# Made by Frend
term = Terminal()
messages = []


def print_clear():
    """
    Clears the screen
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
    messages.append(term.green + "Task added successfully!" + term.normal)
    print_clear()


def check_empty(tasks):
    """
    Checks if there are tasks
    """
    return len(tasks) > 0

# Mark the task as complete


def toggle_task_status(tasks):
    """
    Marks the selected task as complete on the list.
    """
    if check_empty(tasks):
        print_clear()

        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            while messages:
                print(messages.pop(0))
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input(
                "Enter the index of the task to mark as complete:\n "
            )
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(tasks):
                    tasks[index]["complete"] = not tasks[index]["complete"]
                    messages.append(
                        term.green +
                        "Task marked as" +
                        (
                            " complete." if (
                                tasks[index]["complete"]
                            ) else " incomplete."
                        ) +
                        term.normal
                    )
                    print_clear()
                    choice_made = True
                else:
                    messages.append(
                        term.red +
                        "Invalid task index." +
                        term.normal
                    )
                    print_clear()
            elif index.lower() == 'q':
                print_clear()
                choice_made = True
            else:
                messages.append(
                    term.red +
                    "Invalid task index. Should be an integer.\n" +
                    term.normal
                )
                print_clear()
    else:
        messages.append(term.red + "There are no tasks" + term.normal)
        print_clear()


# Task Viewer
def view_tasks(tasks):
    """
    Function to check if the task in question is complete or not.
    """
    if check_empty(tasks):
        print_clear()
        for i, task in enumerate(tasks):
            status = "Complete" if task["complete"] else "Incomplete"
            print(
                term.yellow +
                f"{i}. {task['description']} - {status}" +
                term.normal
            )
    else:
        messages.append(term.red + "There are no tasks" + term.normal)
        print_clear()


# Edit Tasks
def edit_task(tasks):
    """
    A way to Edit tasks if a spelling error occurred,
    or the task it self has changed.
    """
    if check_empty(tasks):
        print_clear()
        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            while messages:
                print(messages.pop(0))
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input("Enter the index of the task to edit:\n")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(tasks):
                    task = tasks[index]
                    new_description = input("Enter new task description:\n")
                    task["description"] = new_description

                    messages.append(
                        term.green +
                        "Task edited successfully!" +
                        term.normal
                    )
                    print_clear()
                    choice_made = True
                else:
                    messages.append(
                        term.red +
                        "Invalid task index." +
                        term.normal
                    )
                    print_clear()

            elif index.lower() == 'q':
                print_clear()
                choice_made = True
            else:
                messages.append(
                    term.red +
                    "Invalid task index. Should be an integer.\n" +
                    term.normal
                )
                print_clear()
    else:
        messages.append(term.red + "There are no tasks" + term.normal)
        print_clear()


# Delete Tasks
def delete_task(tasks):
    """
    A function to Delete tasks if they are not needed
    """
    if check_empty(tasks):
        print_clear()
        print(term.blue + "Tasks:" + term.normal)
        choice_made = False
        while not choice_made:
            while messages:
                print(messages.pop(0))
            view_tasks(tasks)
            print(term.yellow + "q. Press 'q' to go back" + term.normal)
            index = input("Enter the index of the task to delete:\n")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(tasks):
                    del tasks[index]

                    messages.append(
                        term.green +
                        "Task deleted successfully!" +
                        term.normal
                    )
                    print_clear()
                    choice_made = True
                else:

                    messages.append(
                        term.red +
                        "Invalid task index." +
                        term.normal
                    )
                    print_clear()

            elif index.lower() == 'q':
                print_clear()
                choice_made = True
            else:
                messages.append(
                    term.red +
                    "Invalid task index. Should be an integer.\n" +
                    term.normal
                )
                print_clear()
    else:

        messages.append(term.red + "There are no tasks" + term.normal)
        print_clear()


# Main
def main():
    """
    Runs all functions and a simple menu
    """
    tasks = []

    options = [
        "Add task",
        "Toggle task status",
        "View tasks",
        "Edit task",
        "Delete task",
        "Exit"
    ]

    menu = TerminalMenu(options, title="Task manager")
    while True:

        while messages:
            print(messages.pop(0))
        choice = menu.show()
        if choice is not None:
            if options[choice] == "Add task":
                add_task(tasks)
            elif options[choice] == "Toggle task status":
                toggle_task_status(tasks)
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
