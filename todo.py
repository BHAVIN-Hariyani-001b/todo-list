## todo list 
todo_task = []

def add_task():
    """Add to task in the list"""

    user = input("Enter your task : ").strip()
    if user:
        todo_task.append(user)
        print("✅ Task added!")
    else:
        print("⚠️ Empty task not allowed!")

def show_tasks():
    """Show all task"""

    print("\nTODO TASK :")
    if todo_task:
        for i,val in enumerate(todo_task,start=1):
            print(f"{i}. {val}")
    else:
        print("⚠️  No tasks found.")

def edit_task():
    """Edit a task by it's number"""

    show_tasks()
    if not todo_task:
        return
    try:
        user = int(input("Enter your edit task numner : ")) - 1
        if(0 <= user < len(todo_task)):
            edit_taks_input = input("Enter your task : ").strip()
            if edit_taks_input:
                todo_task[user] = edit_taks_input
                print("✏️ Task updated!")
            else:
                print("⚠️  Empty task not allowed!")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
         print("⚠️  Please enter a valid number.")

def delete_task():
    """Delete a task by it's number"""
    show_tasks()
    if not todo_task:
        return

    try:
        user = int(input("Enter your delete task numner : ")) - 1
        if todo_task:
            print(f"🗑️  Task '{todo_task[user]}' deleted.")
            todo_task.pop(user)
        else:
              print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main menu loop"""
    while True:
        print("\n ---- todo list menu ----")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))

            match choice:
                case 1: show_tasks()
                case 2: add_task()
                case 3: edit_task()
                case 4: delete_task()
                case 5:
                    print("Goodbye! 👋")
                    break
                case _:
                    print("⚠️  unvalid choice, try again")
        except ValueError:
            print("⚠️  Please enter a number (1-5).")

# main function call
main()