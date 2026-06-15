from datetime import datetime
# Import validation functions from the sibling module
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list to hold dictionaries globally within this module
tasks = []

def add_task(title, description, due_date):
    """Validates inputs and adds a new task dictionary to the global array."""
    if (validate_task_title(title) and 
        validate_task_description(description) and 
        validate_due_date(due_date)):
        
        new_task = {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    else:
        print("Failed to add task due to validation errors.")
        return False

def mark_task_as_complete(index, tasks=tasks):
    """Marks a pending task as complete based on its 1-indexed list position."""
    try:
        idx = int(index) - 1
        if idx < 0 or idx >= len(tasks):
            print("Error: Task index out of range.")
            return False
        
        if tasks[idx]["completed"]:
            print("Task is already marked as complete.")
            return False
            
        tasks[idx]["completed"] = True
        print("Task marked as complete!")
        return True
    except ValueError:
        print("Error: Please enter a valid numerical index.")
        return False

def view_pending_tasks(tasks=tasks):
    """Displays all tasks that currently have an uncompleted status."""
    pending = [t for t in tasks if not t["completed"]]
    
    if not pending:
        print("\nNo pending tasks found.")
        return
        
    print("\n--- Pending Tasks ---")
    # Enumerate matching the index in the true system list
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"[{i + 1}] Title: {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Due Date: {task['due_date']}")
            print("-" * 20)

def calculate_progress(tasks=tasks):
    """Calculates and reports the ratio of completed tasks to total tasks."""
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("\nProgress: No tasks available to track.")
        return 0.0
        
    completed_tasks = sum(1 for t in tasks if t["completed"])
    progress = (completed_tasks / total_tasks) * 100
    
    print(f"\n--- Progress Report ---")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed: {completed_tasks}")
    print(f"Completion Rate: {progress:.2f}%")
    return progress