from database.db_handler import create_connection, initialize_database, add_task_to_db, get_tasks, mark_task_complete, mark_task_active  # Zorg ervoor dat mark_task_active hier wordt geïmporteerd
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import csv
import openpyxl

def format_date(due_date):
    # Functie om de datum te formatteren
    if "/" in due_date:
        due_date = due_date.replace("/", "-")
    due_date.split("-")
    if len(due_date) == 10 and due_date[4] == '-' and due_date[7] == '-':
        date_parts = due_date.split('-')
        due_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
    return due_date

def add_task():
    title = input("Task: ").strip()
    while not title:
        print("Task cannot be empty.")
        title = input("Task: ").strip()

    description = input("(Description): ").strip()
    due_date = input("Due date (DD-MM-YYYY): ").strip()
    while not due_date:
        print("Due date cannot be empty.")
        due_date = format_date(due_date)

    add_task_to_db(title, description, due_date)
    print(f"Task '{title}' added!")

def view_tasks(completed=False):
    active_tasks = get_tasks(completed=False)
    completed_tasks = get_tasks(completed=True)

    if not completed:
        if active_tasks:
            print("\nActive Tasks:")
            for index, task in enumerate(active_tasks, start=1):
                print(f"{index}. {task['title']} (Due: {task['due_date']})")
                if task['description']:
                    print(f"\t{task['description']}")
        else:
            print("\nNo active tasks found.\n")
    else:  
        if completed_tasks:
            print("\nCompleted Tasks:")
            for index, task in enumerate(completed_tasks, start=1):
                print(f"{index}. {task['title']} (Due: {task['due_date']})")
                if task['description']:
                    print(f"  Description: {task['description']}")
        else:
            print("\nNo completed tasks found.\n")

def mark_task_complete():
    view_tasks() 
    task_id = int(input("Enter task number to mark as complete: "))
    tasks = get_tasks(completed=False)
    if task_id < 1 or task_id > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_id - 1]
    task_id = task["id"]

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    print(f"Task '{task['title']}' is marked as complete.")

def delete_task_from_db(completed=False):
    tasks = get_tasks(completed=completed)
    
    if not tasks:
        print(f"\nNo {'completed' if completed else 'active'} tasks found.\n")
        return
    if completed:
        print("\nCompleted Tasks:")
    else:
        print("\nActive Tasks:")
    
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} (Due: {task['due_date']})")
        if task['description']:
            print(f"  Description: {task['description']}")

    task_id = int(input(f"Enter task ID to delete from {'completed' if completed else 'active'} tasks: "))
    if task_id < 1 or task_id > len(tasks):
        print("Invalid task ID.")
        return

    task_to_delete = tasks[task_id - 1] 

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_to_delete['id'],))
    conn.commit()
    conn.close()

    print(f"Task with ID {task_to_delete['id']} has been deleted.")




def move_task_to_active():
    completed_tasks = get_tasks(completed=True)
    if completed_tasks:
        print("\nCompleted Tasks:")
        for index, task in enumerate(completed_tasks, start=1):
            print(f"{index}. {task['title']} (Due: {task['due_date']})")
            if task['description']:
                print(f"  Description: {task['description']}")
        
        task_number = int(input("Enter task number to move back to active: "))
        if 1 <= task_number <= len(completed_tasks):
            task_id = completed_tasks[task_number - 1]['id']
            mark_task_active(task_id)  # Verplaats taak naar actieve taken
        else:
            print("Invalid task number.")
    else:
        print("No completed tasks to move back.")


def plot_active_VS_completed():
    active_tasks = get_tasks(completed=False)
    completed_tasks = get_tasks(completed=True)

    active_count = len(active_tasks)
    completed_count = len(completed_tasks)

    labels = ['Active', 'Completed']
    counts = [active_count, completed_count]

    plt.bar(labels, counts, color=['green', 'red'])

    plt.title('Task Status Distribution')
    plt.xlabel('Task Status')
    plt.ylabel('Number of Tasks')
    plt.show()

#EXPORT

def export_to_csv():
    tasks = get_tasks(completed=False)
    completed_tasks = get_tasks(completed=True)
    all_tasks = tasks + completed_tasks
    df = pd.DataFrame(all_tasks)

    #kolom headers
    df.columns = ['id', 'title', 'description', 'due_date', 'status']
    df.to_csv('tasks.csv', index=False)
    print("Tasks exported to tasks.csv.")


def export_to_excel():
    # Haal actieve en voltooide taken op
    tasks = get_tasks(completed=False)
    completed_tasks = get_tasks(completed=True)

    # Combineer alle taken in een DataFrame
    active_tasks_df = pd.DataFrame(tasks)
    active_tasks_df["Status"] = "Active"
    completed_tasks_df = pd.DataFrame(completed_tasks)
    completed_tasks_df["Status"] = "Completed"
    
    # Combineer de DataFrames van actieve en voltooide taken
    all_tasks_df = pd.concat([active_tasks_df, completed_tasks_df], ignore_index=True)
    
    # Exporteer naar Excel bestand
    try:
        all_tasks_df.to_excel('tasks_export.xlsx', index=False, sheet_name="Tasks")
        print("Tasks exported successfully to tasks_export.xlsx.")
    except Exception as e:
        print(f"An error occurred while exporting tasks: {e}")




#MENUS:

def export_menu():
    while True:
        print("\nExport menu:")
        print("  1. Export to CSV")
        print("  2. Export to Excel")
        print("  3. Return to main menu")

        choice = int(input("Select an option: "))
        if choice == 1:
            export_to_csv()
        elif choice == 2:
            export_to_excel()
        elif choice == 3:
            break
        else:
            print("Invalid choice.")


def completed_tasks_menu():
    while True:
        print("\nCompleted tasks menu:")
        print("  1. View completed tasks")
        print("  2. Move task back to active")
        print("  3. Remove tasks")
        print("  4. Plot: Active VS Completed tasks")
        print("  5. Return to main menu")

        choice = int(input("Select an option: "))
        if choice == 1:
            view_tasks(completed=True)
        elif choice == 2:
            move_task_to_active()
        elif choice == 3:
            delete_task_from_db(completed=True)
        elif choice == 4:
            plot_active_VS_completed()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\nTo-do list menu:")
        print("  1. Add task")
        print("  2. Show tasks")
        print("  3. Mark task as complete")
        print("  4. Delete task")
        print("  5. Completed tasks menu")
        print("  6. Export tasks menu")
        print("  7. EXIT")

        choice = int(input("Select an option: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_complete()
        elif choice == 4:
            delete_task_from_db(completed=False)
        elif choice == 5:
            completed_tasks_menu()
        elif choice == 6:
            export_menu()  
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    initialize_database()
    main_menu()
