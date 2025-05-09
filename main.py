from auth import login
from inventory import add_item, view_inventory, update_item, delete_item
from order import take_order
from report import sales_report

def admin_menu():
    while True:
        print("1. View Inventory\n2. Add Item\n3. Update Item\n4. Delete Item\n5. View Sales Report\n6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            sales_report()
        elif choice == '6':
            break
        else:
            print("Invalid choice!\n")

def staff_menu():
    while True:
        print("1. Take Order\n2. View Inventory\n3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            take_order()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    print("Welcome to Cafe Management System ☕\n")
    role = login()
    if role == "admin":
        admin_menu()
    elif role == "staff":
        staff_menu()
