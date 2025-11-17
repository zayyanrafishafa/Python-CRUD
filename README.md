# Library Book Management System – Capstone Project

## Overview
The **Library Book Management System** is a Python-based data management project designed to streamline how libraries handle book records, user information, and borrowing transactions.  
It applies the **CRUD (Create, Read, Update, Delete)** concept, enabling efficient management of book inventory, while integrating **data analytics and machine learning** to support smarter decision-making.

The project was developed as part of a capstone assignment to demonstrate practical database operations, data cleaning, and predictive modeling using Python.

---

## Core Features: CRUD Operations

### Create
Add new entries into the system, such as:
- Registering new **books** (title, author, category, and status)
- Adding new **users** (student, teacher, or external member)
- Recording **borrowing transactions**

This ensures that the library can easily expand and track its resources.

---

### Read
Retrieve and view data from the system:
- Display all books or filter by **availability**, **category**, or **status**
- Search for specific books or users
- Generate summary reports such as **most borrowed books**, **active users**, or **borrowing frequency by category**

This allows librarians to monitor library activity and identify usage patterns efficiently.

---

### Update
Modify or correct existing records:
- Change a book’s **status** from “Available” → “Borrowed” or “Returned”
- Update user details or renew borrowing periods
- Edit inaccurate information (e.g., author name or book title)

The update feature ensures that all information remains accurate and up to date.

---

### Delete
Remove outdated or invalid records:
- Delete books that are **lost, damaged, or obsolete**
- Remove **inactive users** or duplicate entries
- Clean up historical data to maintain a lightweight and efficient system

This keeps the dataset clean, relevant, and optimized for reporting.

---

## Extra Features
Beyond CRUD, the project includes additional analytical and intelligent components:
- **📊 Data Visualization:** Charts showing borrowing trends, top book categories, and user activity.
- **🧠 Predictive Analytics:** A Random Forest model predicts **late book returns**, allowing proactive reminders and better inventory planning.
- **📈 Feature Engineering:** Derived metrics like `Borrow_Duration` and `User_Activity_Score` help understand borrowing behavior.
- **💡 Recommendation System (Future Scope):** Suggests books or categories based on user borrowing history.

---

## Tools and Technologies
| Category | Tools Used |
|-----------|-------------|
| Language | Python 3 |
| Data Handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn |
| Model Evaluation | accuracy_score, classification_report |
| Deployment (optional) | Streamlit / Flask |

---

## Project Impact
This capstone demonstrates how **Python CRUD operations** can be combined with **analytics and prediction** to create a modern, data-driven library management system.  
It allows libraries to:
- Manage library book database  
- Track user activity and late returns as well as calculate the fine for late return  
- Make data-backed decisions for book acquisition and retention  
