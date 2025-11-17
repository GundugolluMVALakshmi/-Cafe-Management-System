# db_config.py
import sqlite3
from contextlib import closing

DB_NAME = "cafe.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with closing(get_db_connection()) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            quantity INTEGER,
            total_price REAL,
            order_time TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
        # insert sample users if not exists
        cur.execute("SELECT COUNT(*) FROM users")
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
                        ("admin", "admin123", "admin"))
            cur.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
                        ("staff", "staff123", "staff"))
        # insert sample inventory if empty
        cur.execute("SELECT COUNT(*) FROM inventory")
        if cur.fetchone()[0] == 0:
            sample = [
                ("Coffee", 40.0, 50),
                ("Tea", 20.0, 50),
                ("Sandwich", 60.0, 30),
                ("Burger", 80.0, 20),
                ("Pizza", 120.0, 10)
            ]
            cur.executemany("INSERT INTO inventory (name, price, quantity) VALUES (?, ?, ?)", sample)
        conn.commit()
