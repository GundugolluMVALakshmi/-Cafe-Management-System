# order.py
from db_config import get_db_connection

def take_order():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    items = cur.fetchall()

    print("\nMenu:")
    for it in items:
        print(f"{it['item_id']}. {it['name']} - ₹{it['price']} (stock: {it['quantity']})")

    cart = []
    while True:
        iid = input("Enter item id (or 'done'): ").strip()
        if iid.lower() == 'done':
            break
        try:
            item_id = int(iid)
        except ValueError:
            print("Invalid id. Try again.")
            continue
        qty = int(input("Quantity: ").strip())
        cart.append((item_id, qty))

    if not cart:
        print("No items selected.\n")
        conn.close()
        return

    # check stock and calculate total
    total = 0
    for item_id, qty in cart:
        cur.execute("SELECT name, price, quantity FROM inventory WHERE item_id=?", (item_id,))
        row = cur.fetchone()
        if not row:
            print(f"Item id {item_id} not found. Order cancelled.\n")
            conn.close()
            return
        if row["quantity"] < qty:
            print(f"Not enough stock for {row['name']}. Available: {row['quantity']}. Order cancelled.\n")
            conn.close()
            return
        total += row["price"] * qty

    # create order and update stock
    for item_id, qty in cart:
        cur.execute("SELECT name, price, quantity FROM inventory WHERE item_id=?", (item_id,))
        row = cur.fetchone()
        cur.execute("INSERT INTO orders (item_name, quantity, total_price) VALUES (?, ?, ?)",
                    (row["name"], qty, row["price"] * qty))
        new_qty = row["quantity"] - qty
        cur.execute("UPDATE inventory SET quantity=? WHERE item_id=?", (new_qty, item_id))

    conn.commit()
    print(f"\nOrder placed successfully! Total: ₹{total}\n")
    conn.close()
