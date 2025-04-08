def todo_list():
    tasks = []
    
    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"'{task}' has been added to your to-do list.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"'{task}' has been removed.")
            else:
                print(f"Task '{task}' not found.")
        elif choice == '3':
            if tasks:
                print("\nYour To-Do List:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("Your to-do list is empty.")
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice, try again.")

# Run the to-do list
todo_list()
