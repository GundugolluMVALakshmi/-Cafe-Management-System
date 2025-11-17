# auth.py
from db_config import get_db_connection

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    row = cur.fetchone()
    conn.close()

    if row:
        role = row["role"]
        print(f"Login successful as {role}!\n")
        return role
    else:
        print("Invalid credentials.\n")
        return None
