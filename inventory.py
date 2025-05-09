from db_config import get_db_connection

def add_item():
    name = input("Item name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
    conn.commit()
    conn.close()
    print("Item added successfully!\n")

def view_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    conn.close()
    print("Current Inventory:")
    for row in rows:
        print(row)

def update_item():
    item_id = int(input("Enter item ID to update: "))
    new_price = float(input("New price: "))
    new_quantity = int(input("New quantity: "))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET price=%s, quantity=%s WHERE item_id=%s", (new_price, new_quantity, item_id))
    conn.commit()
    conn.close()
    print("Item updated successfully!\n")

def delete_item():
    item_id = int(input("Enter item ID to delete: "))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE item_id=%s", (item_id,))
    conn.commit()
    conn.close()
    print("Item deleted successfully!\n")
