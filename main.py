import os
import sys
from task import TaskManager

# ---- CONSTANTS ---- #
COLOR_HIGH = "\033[91m"
COLOR_MED = "\033[93m"
COLOR_LOW = "\033[92m"
COLOR_RESET = "\033[0m"

tm = TaskManager()

def print_menu():
    print(f"\n---  TASK MANAGER ---")
    print(f"1. Add Task")
    print(f"2. List All Tasks")
    print(f"3. Mark Task Completed")
    print(f"4. Delete Task")
    print(f"5. Filter Tasks")
    print(f"6. Exit")

def print_tasks(tasks):
    if len(tasks) == 0:
        print(f"No tasks found! ")
        return
        
    for t in tasks:
        color = COLOR_RESET
        if t["priority"] == "high":
            color = COLOR_HIGH
        elif t["priority"] == "medium":
            color = COLOR_MED
        elif t["priority"] == "low":
            color = COLOR_LOW
            
        status = "" if t["completed"] else ""
        date_str = f" [Due: {t['due_date']}]" if t["due_date"] else ""
        print(f"{t['id']}. {status} {color}{t['title']}{COLOR_RESET} ({t['priority']}){date_str}")

def main():
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            title = input("Task title: ").strip()
            priority = input("Priority (high/medium/low): ").strip().lower()
            if priority not in ["high", "medium", "low"]:
                priority = "medium"
            due_date = input("Due date (optional): ").strip()
            
            t_id = tm.add_task(title, priority, due_date)
            print(f"Task added with ID: {t_id} ")
            
        elif choice == "2":
            tasks = tm.get_all_tasks()
            print_tasks(tasks)
            
        elif choice == "3":
            try:
                t_id = int(input("Enter task ID to mark complete: ").strip())
                if tm.mark_completed(t_id):
                    print(f"Task {t_id} marked as complete! ")
                else:
                    print(f"Task ID not found.")
            except Exception as e:
                print(f"Invalid input: {e}")
                
        elif choice == "4":
            try:
                t_id = int(input("Enter task ID to delete: ").strip())
                if tm.delete_task(t_id):
                    print(f"Task {t_id} deleted! ")
                else:
                    print(f"Task ID not found.")
            except Exception as e:
                print(f"Invalid input: {e}")
                
        elif choice == "5":
            print(f"1. Filter by priority")
            print(f"2. Filter by status")
            sub = input("Choice: ").strip()
            
            if sub == "1":
                p = input("Enter priority (high/medium/low): ").strip().lower()
                tasks = tm.get_all_tasks(filter_priority=p)
                print_tasks(tasks)
            elif sub == "2":
                s = input("Enter status (completed/pending): ").strip().lower()
                status_bool = True if s == "completed" else False
                tasks = tm.get_all_tasks(filter_status=status_bool)
                print_tasks(tasks)
            else:
                print(f"Invalid choice.")
                
        elif choice == "6":
            print(f"Goodbye! ")
            break
        else:
            print(f"Invalid choice, try again.")

if __name__ == "__main__":
    main()
