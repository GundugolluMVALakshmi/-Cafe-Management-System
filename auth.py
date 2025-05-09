from db_config import get_db_connection

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        print(f"Login successful as {result[0]}!\n")
        return result[0]
    else:
        print("Invalid credentials.\n")
        return None
