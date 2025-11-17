# report.py
from db_config import get_db_connection

def sales_report():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT order_id, item_name, quantity, total_price, order_time FROM orders ORDER BY order_time DESC")
    rows = cur.fetchall()
    conn.close()
    print("\nSales Report:")
    total_sales = 0
    for r in rows:
        print(f"Order {r['order_id']} | {r['item_name']} x{r['quantity']} = ₹{r['total_price']} | {r['order_time']}")
        total_sales += r['total_price']
    print(f"\nTotal Sales: ₹{total_sales}\n")
