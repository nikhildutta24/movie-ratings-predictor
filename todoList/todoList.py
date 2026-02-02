tasks = []

def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Quit")

while True:
    display_menu()
    choice = input("Input choice: ")

    if choice == '1':
        task = input("Input task: ")
        tasks.append(task)
        print("Task successfully added")

    elif choice == '2':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task = input("Enter new task name: ")
                    tasks[task_index] = new_task
                    print("Edit saved successfully")
                else:
                    print("Invalid index")
            except ValueError:
                print("Invalid input")
        else:
            print("No tasks available")

    elif choice == '3':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task to be deleted: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)
                    print("Task successfully deleted")
                else:
                    print("Invalid index")
            except ValueError:
                print("Invalid input")
        else:
            print("No tasks available")

    elif choice == '4':
        print("Exiting the application. Thank you!")
        break

    else:
        print("Invalid choice")
