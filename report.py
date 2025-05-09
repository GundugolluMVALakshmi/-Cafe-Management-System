from db_config import get_db_connection

def sales_report():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    total_sales = sum(row[3] for row in rows)
    print("Sales Report:")
    for row in rows:
        print(row)
    print(f"Total Sales: ₹{total_sales}\n")
    conn.close()
