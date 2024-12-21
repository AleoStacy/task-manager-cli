from helpers import add_task, list_tasks, complete_task, delete_task

def main():
    print("Welcome to the Task Manager CLI!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("Exiting Task Manager CLI. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
