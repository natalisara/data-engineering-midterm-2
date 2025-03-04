import sqlite3

DB_PATH = "data/database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    with open("data/init_db.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# ბაზის ინიციალიზაცია
initialize_database()
