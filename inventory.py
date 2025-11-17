# inventory.py
from db_config import get_db_connection

def add_item():
    name = input("Item name: ").strip()
    price = float(input("Price: ").strip())
    quantity = int(input("Quantity: ").strip())

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (name, price, quantity) VALUES (?, ?, ?)",
                (name, price, quantity))
    conn.commit()
    conn.close()
    print("Item added successfully!\n")


def view_inventory():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    conn.close()

    print("\nCurrent Inventory:")
    print("-" * 50)
    print(f"{'ID':<5} {'Name':<15} {'Price':<10} {'Quantity':<10}")
    print("-" * 50)

    for row in rows:
        print(f"{row['item_id']:<5} {row['name']:<15} ₹{row['price']:<10} {row['quantity']:<10}")

    print("-" * 50 + "\n")

def update_item():
    item_id = int(input("Enter item ID to update: ").strip())
    new_price_input = input("New price (leave blank to keep): ").strip()
    new_qty_input = input("New quantity (leave blank to keep): ").strip()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE item_id=?", (item_id,))
    item = cur.fetchone()

    if not item:
        print("Item not found.\n")
        conn.close()
        return

    new_price = float(new_price_input) if new_price_input else item["price"]
    new_qty = int(new_qty_input) if new_qty_input else item["quantity"]

    cur.execute("UPDATE inventory SET price=?, quantity=? WHERE item_id=?",
                (new_price, new_qty, item_id))
    conn.commit()
    conn.close()
    print("Item updated successfully!\n")

def delete_item():
    item_id = int(input("Enter item ID to delete: ").strip())

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory WHERE item_id=?", (item_id,))
    conn.commit()
    conn.close()
    print("Item deleted successfully!\n")
