import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",  # Replace with your MySQL password
        database="cafe_db"
    )
