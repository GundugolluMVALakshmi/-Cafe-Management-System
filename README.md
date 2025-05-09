---

# ☕ Cafe Management System

A simple and efficient **Inventory & Billing System** designed using Python and MySQL for managing daily cafe operations. Now enhanced with a 🔐 **Role-Based Login System** for secure access control.

---

## 🚀 Features

* 🔐 **Role-Based Login System**
  Admin and Staff login with restricted access based on roles.

* 📋 **Inventory Management**
  Add, update, delete items and track stock in real time.

* 💰 **Order Processing & Billing**
  Generate bills instantly with item-wise breakdown.

* 📊 **Sales & Inventory Reports**
  Admins can generate daily reports to monitor sales and stock levels.

* 🛠️ **CRUD Operations**
  Full Create, Read, Update, Delete support for inventory items.

---

## 👩‍💼 Roles & Access

| Role  | Access                                           |
| ----- | ------------------------------------------------ |
| Admin | Inventory Management, Sales Reports, Full Access |
| Staff | Take Orders, Generate Bills                      |

---

💯 Sare Mona! 💻 **Technologies Used** section ni inka 👌 attractive ga, clear ga elaborate cheyyadam jarigindi. Ikkada final update 👇

---

## 🧑‍💻 Technologies Used

* 🐍 **Python**
  Used as the core programming language to build the logic for inventory, billing, user interface, and file handling.

* 🛢️ **MySQL**
  Backend relational database system for storing user credentials, item data, and transaction records securely.

* 🧮 **SQL Queries**
  Used for performing CRUD operations (INSERT, SELECT, UPDATE, DELETE) on the MySQL database.

* 🔁 **CRUD Operations**
  Full support for managing the inventory — adding new items, updating prices/quantities, deleting items, and viewing all products.

* 🔐 **Login Authentication System**
  Role-based authentication implemented to allow **Admins** full control and **Staff** limited access (like order billing).

* 🖥️ **Modular Programming**
  Separated functionalities into different Python files like `auth.py`, `inventory.py`, `order.py`, etc., for clean code structure and easy maintenance.

* 📈 **Console-based Interface**
  Interactive terminal menu system designed for both Admins and Staff to perform operations smoothly without GUI.


---

## 🏗️ Folder Structure

```
CafeManagementSystem/
│
├── main.py                  # Main executable file
├── db_config.py             # MySQL database connection setup
├── auth.py                  # Role-based login logic
├── inventory.py             # CRUD operations for inventory
├── order.py                 # Billing and order handling
├── report.py                # Sales and inventory reports
├── schema.sql               # SQL script to create tables
├── README.md                # Project overview
└── requirements.txt         # Dependencies (if any)
```

---

## 🧪 Sample Users

| Username | Password | Role  |
| -------- | -------- | ----- |
| admin    | admin123 | admin |
| staff    | staff123 | staff |

---

## 📸 Sample Output

```bash
Welcome to Cafe Management System ☕
Enter username: admin
Enter password: ******
Login successful as admin!

1. Manage Inventory
2. View Reports
3. Take Order
4. Logout
Enter your choice: _
```

---

