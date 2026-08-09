FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks and their completion status from text file."""
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Expecting format: task_name|status (e.g., "Buy milk|0")
                    if "|" in line:
                        title, status = line.rsplit("|", 1)
                        tasks.append({"title": title, "done": status == "1"})
                    else:
                        # Fallback for old task file formats without status
                        tasks.append({"title": line, "done": False})
    except FileNotFoundError:
        pass  # File will be created on first save
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Save tasks and their completion status to text file."""
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                status = "1" if task["done"] else "0"
                file.write(f"{task['title']}|{status}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def view_tasks(tasks):
    """Display a formatted, numbered list of tasks with completion status."""
    if not tasks:
        print("\n Your to-do list is empty!")
        return
    
    print("\n================ YOUR TO-DO LIST ================")
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")
    print("=================================================")

def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("\nEnter new task: ").strip()
    if task_name:
        tasks.append({"title": task_name, "done": False})
        save_tasks(tasks)
        print(f" Task '{task_name}' added successfully!")
    else:
        print("Task cannot be empty.")

def mark_completed(tasks):
    """Mark an existing task as completed."""
    if not tasks:
        print("\nNo tasks to complete!")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            task["done"] = True
            save_tasks(tasks)
            print(f" Marked '{task['title']}' as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    """Remove a task by number."""
    if not tasks:
        print("\nNo tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f" Removed task: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=========================")
        print("    TO-DO LIST APP")
        print("=========================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()