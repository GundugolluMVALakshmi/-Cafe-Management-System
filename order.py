from db_config import get_db_connection

def take_order():
    item_id = int(input("Enter item ID: "))
    qty = int(input("Enter quantity: "))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, quantity FROM inventory WHERE item_id=%s", (item_id,))
    item = cursor.fetchone()

    if item and item[2] >= qty:
        item_name, price, available_qty = item
        total = price * qty

        cursor.execute("UPDATE inventory SET quantity = quantity - %s WHERE item_id = %s", (qty, item_id))
        cursor.execute("INSERT INTO orders (item_name, quantity, total_price) VALUES (%s, %s, %s)", (item_name, qty, total))
        conn.commit()
        print(f"\nOrder placed successfully!\nItem: {item_name}\nQuantity: {qty}\nTotal: ₹{total}\n")
    else:
        print("Not enough stock or invalid item ID.\n")
    conn.close()
