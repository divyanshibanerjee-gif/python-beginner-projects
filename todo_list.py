tasks = []

while True:

    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = int(input("Enter task number to delete: "))

            if task_number >= 1 and task_number <= len(tasks):

                deleted_task = tasks.pop(task_number - 1)

                print("Deleted:", deleted_task)

            else:
                print("Invalid task number!")

    elif choice == "4":

        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice! Please try again.")
