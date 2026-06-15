# Import functions cleanly from the task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Create New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            print("\n--- Mark Task Complete ---")
            # Displays currently pending tasks to assist the user with indexing
            view_pending_tasks()
            index = input("Enter the number of the task to complete: ")
            mark_task_as_complete(index)
            
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            calculate_progress()
            
        elif choice == "5":
            print("Exiting the program...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()