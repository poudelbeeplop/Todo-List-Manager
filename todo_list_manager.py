import sqlite3
import argparse
import re
from datetime import datetime

conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    status INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def add_task(task_description):
    if not validate_task(task_description):
         print("ERROR: Task description contains invaild characters.")
         return
    

    cursor.execute('''
    INSERT INTO tasks (task, status) 
    VALUES (?, ?)
    ''', (task_description, 0)) 
    conn.commit()
    print(f"Task '{task_description}' added successfully.")


def remove_task(task_id):
    cursor.execute('''
    DELETE FROM tasks WHERE id = ?
    ''', (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} has been removed.")

def complete_task(task_id):
    cursor.execute('''
    UPDATE tasks SET status = 1 WHERE id = ?
    ''', (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} marked as completed.")


def list_tasks():
    cursor.execute('''
    SELECT id, task, status, created_at FROM tasks
    ''')
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task[2] == 1 else "Incomplete"
            print(f"ID: {task[0]}, Task: {task[1]}, Status: {status}, Created At: {task[3]}")

 
def validate_task(task_description):
    pattern = r'^[a-zA-Z0-9\s]+$'
    return bool(re.match(pattern, task_description))
   

def parse_args():
    parser = argparse.ArgumentParser(description="Todo List Manager")
    parser.add_argument("-a", "--add", type=str, help="Add a new task")
    parser.add_argument("-r", "--remove", type=int, help="Remove a task by ID")
    parser.add_argument("-c", "--complete", type=int, help="Mark a task as completed by ID")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    return parser.parse_args()

# Main fuction to execute the scriptt
def main():
    args = parse_args()

    if args.add:
        add_task(args.add)
    elif args.remove:
        remove_task(args.remove)
    elif args.complete:
        complete_task(args.complete)
    elif args.list:
        list_tasks()
    else:
        print("Invalid arguments. Use -h or --help for usage information.")

if __name__ == "__main__":
    main()
