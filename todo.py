## todo list program ##
# Simple CLI-based TODO List app with Add, Show, Edit, and Delete functionality

todo_task = []  # Global list to store tasks


def add_task():
    """Add a new task to the list"""
    user = input("Enter your task : ").strip()
    if user:
        todo_task.append(user)   # Add non-empty task
        print("✅ Task added!")
    else:
        print("⚠️ Empty task not allowed!")


def show_tasks():
    """Show all tasks"""
    print("\nTODO TASK :")
    if todo_task:   # Check if list has tasks
        for i, val in enumerate(todo_task, start=1):  # Show with numbering
            print(f"{i}. {val}")
    else:
        print("⚠️  No tasks found.")


def edit_task():
    """Edit a task by its number"""
    show_tasks()  # Show tasks before editing
    if not todo_task:
        return  # Exit if no tasks present
    try:
        user = int(input("Enter your edit task number : ")) - 1
        if 0 <= user < len(todo_task):  # Valid index check
            edit_taks_input = input("Enter your new task : ").strip()
            if edit_taks_input:
                todo_task[user] = edit_taks_input  # Replace old task
                print("✏️ Task updated!")
            else:
                print("⚠️  Empty task not allowed!")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")


def delete_task():
    """Delete a task by its number"""
    show_tasks()
    if not todo_task:
        return  # Exit if no tasks present

    try:
        user = int(input("Enter your delete task number : ")) - 1
        if 0 <= user < len(todo_task):  # Ensure index is valid
            print(f"🗑️  Task '{todo_task[user]}' deleted.")
            todo_task.pop(user)  # Remove from list
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main menu loop"""
    while True:
        # Show main menu
        print("\n ---- TODO List Menu ----")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))

            match choice:  # Match-case structure (Python 3.10+)
                case 1: show_tasks()
                case 2: add_task()
                case 3: edit_task()
                case 4: delete_task()
                case 5:
                    print("Goodbye! 👋")
                    break
                case _:
                    print("⚠️  Invalid choice, try again")
        except ValueError:
            print("⚠️  Please enter a number (1-5).")


# Start the program
main()
