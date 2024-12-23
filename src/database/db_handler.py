import sqlite3
from Config.config import db_path

def create_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Zorg voor dict-achtige rijen
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
    print("Database geïnitialiseerd!")

def add_task_to_db(title, description, due_date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (title, description, due_date, completed)
    VALUES (?, ?, ?, 0)
    """, (title, description, due_date))

    conn.commit()
    conn.close()

def get_tasks(completed=False):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE completed = ?", (completed,))
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def mark_task_complete(task_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def mark_task_active(task_id):
    conn = create_connection()
    cursor = conn.cursor()

    # Update de taak om 'completed' terug naar 0 (niet voltooid) te zetten
    cursor.execute("UPDATE tasks SET completed = 0 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task with ID {task_id} has been moved back to active.")
