import sqlite3

DATABASE = "database/interview.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password TEXT

    )
    """)

    conn.commit()

    conn.close()