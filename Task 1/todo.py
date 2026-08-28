# CODSOFT Internship
# Task 1 - To-Do List

tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)


def add_task():
    task = input("\nEnter task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


def update_task():
    show_tasks()

    if len(tasks) > 0:
        try:
            number = int(input("\nEnter task number to update: "))

            if 1 <= number <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if len(tasks) > 0:
        try:
            number = int(input("\nEnter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
