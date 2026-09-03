"""Program 12: To-Do List Application
A simple command-line to-do list manager with add, view, complete, and delete operations."""
import json
import os

TODO_FILE = "todos.json"


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add_task(todos):
    task = input("Enter the task: ").strip()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print(f"Added: {task}")
    else:
        print("Task cannot be empty.")


def view_tasks(todos):
    if not todos:
        print("No tasks found.")
        return
    print("\n--- To-Do List ---")
    for i, item in enumerate(todos, 1):
        status = "[x]" if item["done"] else "[ ]"
        print(f"{i}. {status} {item['task']}")
    print("------------------\n")


def complete_task(todos):
    view_tasks(todos)
    if not todos:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            save_todos(todos)
            print(f"Marked complete: {todos[num - 1]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(todos):
    view_tasks(todos)
    if not todos:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    todos = load_todos()
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task(todos)
        elif choice == "2":
            view_tasks(todos)
        elif choice == "3":
            complete_task(todos)
        elif choice == "4":
            delete_task(todos)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
