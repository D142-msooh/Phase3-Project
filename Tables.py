import sqlite3
from Database import get_connection
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            main_goal TEXT,
            free_hours INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            skill TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            entry TEXT,
            date TEXT
        );
    """)

    conn.commit()
    conn.close()