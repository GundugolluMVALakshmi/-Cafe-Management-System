# main.py
from db_config import init_db
from auth import login
from inventory import add_item, view_inventory, update_item, delete_item
from order import take_order
from report import sales_report

def manage_inventory():
    while True:
        print("\nInventory Management")
        print("1. List Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Back")
        c = input("Enter choice: ").strip()
        if c == "1":
            view_inventory()
        elif c == "2":
            add_item()
        elif c == "3":
            update_item()
        elif c == "4":
            delete_item()
        elif c == "5":
            break
        else:
            print("Invalid choice")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Manage Inventory")
        print("2. View Reports")
        print("3. Logout")
        c = input("Enter choice: ").strip()
        if c == "1":
            manage_inventory()
        elif c == "2":
            sales_report()
        elif c == "3":
            break
        else:
            print("Invalid choice")

def staff_menu():
    while True:
        print("\nStaff Menu")
        print("1. Take Order")
        print("2. View Inventory")
        print("3. Logout")
        c = input("Enter choice: ").strip()
        if c == "1":
            take_order()
        elif c == "2":
            view_inventory()
        elif c == "3":
            break
        else:
            print("Invalid choice")

def main():
    init_db()
    print("Welcome to Cafe Management System ☕\n")
    while True:
        role = login()
        if role == "admin":
            admin_menu()
            break
        elif role == "staff":
            staff_menu()
            break
        else:
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                break

if __name__ == "__main__":
    main()
