# ☕ Café Management System – Python + MySQL

A simple and efficient **Inventory & Billing System** built using **Python** and **MySQL**, designed to manage daily café operations.  
Now enhanced with a **🔐 Role-Based Login System** for secure and structured access.

---

## 🚀 Features

### 🔐 Role-Based Login System
- Admin and Staff login  
- Role restrictions applied automatically  
- Admin → full control  
- Staff → order/billing only  

### 📋 Inventory Management
- Add items  
- Update price/quantity  
- Delete items  
- View stock in real time  

### 💰 Order Processing & Billing
- Generate customer bills  
- Item-wise bill breakdown  
- Total with quantity calculation  

### 📊 Sales & Inventory Reports
- Daily sales reports  
- Stock status  
- Admin-only access  

### 🛠️ CRUD Operations
- Full Create, Read, Update, Delete support using MySQL  

---

## 👩‍💼 Roles & Access

| Role   | Access                                      |
|--------|----------------------------------------------|
| Admin  | Inventory, Reports, Full Access              |
| Staff  | Order Taking, Billing Only                   |

---

## 🧑‍💻 Technologies Used

### 🐍 Python  
Used for business logic, billing system, menu interface, file handling.

### 🛢️ MySQL  
Relational database storing:  
- User credentials  
- Items & stock  
- Sales records  
- Transaction history  

### 🧮 SQL Queries  
Used for CRUD operations (INSERT, SELECT, UPDATE, DELETE).

### 🔐 Login Authentication  
Role-based access implemented using a secure credential check.

### 🖥️ Modular Programming  
Separated into multiple Python modules for clean maintainable code:
- auth.py  
- inventory.py  
- order.py  
- report.py  

### 📈 Console-Based UI  
Smooth text-based interface for both Admin & Staff.

---

## 🏗️ Folder Structure

```
CafeManagementSystem/
│
├── main.py            # Main executable file
├── db_config.py       # MySQL database connection setup
├── auth.py            # Role-based login logic
├── inventory.py       # CRUD operations for inventory
├── order.py           # Billing and order handling
├── report.py          # Sales and inventory reports
├── schema.sql         # SQL script to create DB tables
├── README.md          # Documentation
└── requirements.txt   # Dependencies (if any)
```

---

## 🧪 Sample Users

| Username | Password  | Role  |
|----------|-----------|-------|
| admin    | admin123  | admin |
| staff    | staff123  | staff |

---

## 📸 Sample Output

```
Welcome to Café Management System ☕
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

## ✨ Created By  
**Gundugollu Mohana Venkata Achuta Lakshmi**  
*(Self-Initiated Project)*

🌟 If you like this project, give it a **star ⭐**!
