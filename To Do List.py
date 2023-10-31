Task = []


def display_menu():
    print("Menu")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")


def get_choice():
    return int(input("Please Choose an Option: "))


def get_desc():
    return input("Add you task to the List: ")


def view_tasks(t):
    print("Here is you current To-Do List", t)


def get_task_index():
    return int(input("Which task in the list would you like to modify?: "))


def completed(i):
    comp = "Completed!"
    Task[i] = comp


def remove_task(i):
    print("Removed")
    Task.pop(i)


while True:
    display_menu()
    choice = get_choice()

    if choice == 1:
        task_desc = get_desc()
        Task.append(task_desc)

    elif choice == 2:
        view_tasks(Task)

    elif choice == 3:
        index = get_task_index()
        completed(index)

    elif choice == 4:
        index = get_task_index()
        remove_task(index)

    elif choice == 5:
        break
