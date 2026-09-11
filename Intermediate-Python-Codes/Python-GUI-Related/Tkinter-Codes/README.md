# Python Tkinter GUI Examples

A collection of **beginner-friendly Python GUI examples using Tkinter**.

These examples demonstrate how to build simple desktop applications and connect Tkinter with common Python data-handling tasks such as:

- Displaying a welcome message
- Working with `datetime`
- Reading CSV data with Pandas
- Displaying CSV data in a Tkinter table
- Reading JSON data
- Displaying JSON records in a Tkinter GUI

---

## 📁 Project Structure

```text
Tkinter-Codes/
│
├── Display-Welcome-Message.png
├── Display-Welcome-Msg-0.py
├── Display-Welcome-Msg-1.py
├── Display-Welcome-Msg-2.py
├── Display-Welcome-Msg-GUI.py
│
├── Python-Display-CSV-Data-1.py
├── Python-Display-CSV-Data-2.py
├── Python-Display-CSV-Data.png
│
├── Python-Display-JSON-File-1.py
├── Python-Display-JSON-File-2.py
├── Python-Display-JSON-Data.png
│
├── transactions.csv
└── users.json
```

---

# 🖥️ 1. Display a Welcome Message

The first group of programs demonstrates a very simple Tkinter GUI.

The user enters their name and clicks **Submit**.

The application displays:

```text
Welcome, John Doe!
Wednesday, September 10, 2026 10:30 PM
```

The program uses:

- `tkinter`
- `Entry`
- `Label`
- `Button`
- Functions
- `datetime`
- `strftime()`

### Versions

| File | Description |
|---|---|
| `Display-Welcome-Msg-0.py` | Basic version |
| `Display-Welcome-Msg-1.py` | Same application with detailed comments |
| `Display-Welcome-Msg-2.py` | More compact version |
| `Display-Welcome-Msg-GUI.py` | GUI version with explanatory comments |

### Run

```bash
python Display-Welcome-Msg-0.py
```

---

# 📊 2. Read CSV Data and Display It in a Table

The CSV examples demonstrate how to read a CSV file using **Pandas** and display the data using Tkinter's `Treeview` widget.

The sample file is:

```text
transactions.csv
```

It contains transaction information such as:

```text
TransactionID
Date
Time
Item
Quantity
PricePerItem
TotalPrice
PaymentMethod
```

Example:

| TransactionID | Item | Quantity | PricePerItem | TotalPrice | PaymentMethod |
|---|---|---:|---:|---:|---|
| TX1001 | Cappuccino | 1 | 3.50 | 3.50 | Credit Card |
| TX1002 | Latte | 2 | 4.00 | 8.00 | Cash |
| TX1003 | Espresso | 1 | 2.75 | 2.75 | Mobile Pay |

---

## How the CSV Application Works

The basic flow is:

```text
transactions.csv
       ↓
   Pandas
       ↓
  DataFrame
       ↓
 Tkinter Treeview
       ↓
   GUI Table
```

### Important Code

Read the CSV:

```python
df = pd.read_csv("transactions.csv")
```

Get column names:

```python
df.columns
```

Create the table:

```python
table = ttk.Treeview(
    root,
    columns=list(df.columns),
    show="headings"
)
```

Loop through the DataFrame:

```python
for row in df.itertuples(index=False):
    table.insert("", "end", values=row)
```

---

## CSV Versions

| File | Description |
|---|---|
| `Python-Display-CSV-Data-1.py` | Simple version |
| `Python-Display-CSV-Data-2.py` | Same application with detailed comments |

### Run

Make sure `transactions.csv` is in the same folder as the Python file.

Then run:

```bash
python Python-Display-CSV-Data-1.py
```

or:

```bash
python Python-Display-CSV-Data-2.py
```

---

# 🧾 3. Read JSON Data and Display It in Tkinter

The JSON examples demonstrate how to read a JSON file and display user information in a Tkinter GUI.

The sample file is:

```text
users.json
```

The JSON data contains information such as:

- First name
- Last name
- Age
- Email
- Phone number
- Hobbies

The program also demonstrates accessing **nested JSON data**.

For example:

```python
user["contactDetails"]["emailAddress"]
```

---

## How the JSON Application Works

```text
users.json
    ↓
 json.load()
    ↓
Python List
    ↓
Python Dictionaries
    ↓
Tkinter Labels
    ↓
GUI
```

Read the JSON file:

```python
with open("users.json") as f:
    users = json.load(f)
```

Loop through the users:

```python
for user in users:
```

Access user information:

```python
user["firstName"]
user["lastName"]
user["age"]
```

Access nested information:

```python
user["contactDetails"]["emailAddress"]
```

Access a list:

```python
", ".join(user["hobbies"])
```

---

## JSON Versions

| File | Description |
|---|---|
| `Python-Display-JSON-File-1.py` | Simple version |
| `Python-Display-JSON-File-2.py` | Same application with detailed comments |

### Run

Make sure `users.json` is in the same folder.

```bash
python Python-Display-JSON-File-1.py
```

---

# 📦 Requirements

## Python

Install Python 3.x.

Check your installation:

```bash
python --version
```

## Tkinter

Tkinter is normally included with standard Python installations on Windows.

Test it:

```bash
python -m tkinter
```

If a small Tkinter window opens, Tkinter is working.

## Pandas

The CSV examples require Pandas.

Install it with:

```bash
pip install pandas
```

Or:

```bash
python -m pip install pandas
```

---

# 🚀 Quick Start

Clone/download the project and open the project directory:

```bash
cd Tkinter-Codes
```

Run the welcome application:

```bash
python Display-Welcome-Msg-0.py
```

Run the CSV viewer:

```bash
python Python-Display-CSV-Data-1.py
```

Run the JSON viewer:

```bash
python Python-Display-JSON-File-1.py
```

---

# 🧠 Concepts Covered

## Tkinter

- `Tk()`
- `Label`
- `Entry`
- `Button`
- `Treeview`
- `pack()`
- `config()`
- `mainloop()`

## Python

- Variables
- Functions
- Lists
- Dictionaries
- Loops
- String formatting
- File handling
- Modules
- Nested data

## Date and Time

```python
from datetime import datetime
```

Example:

```python
datetime.now()
```

Formatting:

```python
datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
```

## Pandas

```python
import pandas as pd
```

Read CSV:

```python
pd.read_csv()
```

DataFrame:

```python
df
```

Column names:

```python
df.columns
```

Rows:

```python
df.itertuples()
```

## JSON

```python
import json
```

Read JSON:

```python
json.load()
```

---

# 🔄 CSV vs JSON

| CSV | JSON |
|---|---|
| Tabular data | Structured data |
| Rows and columns | Objects and lists |
| Excellent for spreadsheets | Excellent for APIs/configuration |
| Easy to read with Pandas | Easy to read with `json` |
| Example: transactions | Example: users |

### CSV

```text
ID,Name,Age
1,John,22
2,Jane,21
```

### JSON

```json
[
    {
        "name": "John",
        "age": 22
    },
    {
        "name": "Jane",
        "age": 21
    }
]
```

---

# 🎯 Learning Progression

A recommended learning order for beginners:

```text
1. Display-Welcome-Msg-0.py
             ↓
2. Display-Welcome-Msg-1.py
             ↓
3. Display-Welcome-Msg-2.py
             ↓
4. JSON Viewer
             ↓
5. CSV Viewer
             ↓
6. Tkinter Treeview
             ↓
7. Add Search / Filter
             ↓
8. Add / Edit / Delete Records
             ↓
9. Connect SQLite Database
             ↓
10. Build a Complete CRUD Application
```

---

# 💡 Suggested Next Projects

After completing these examples, try building:

### Student Information Viewer

Read:

```text
students.csv
```

and display:

```text
ID | Name | Age | Course
```

### Employee Viewer

Display:

```text
Employee ID | Name | Department | Salary
```

### Expense Tracker

Store:

```text
Date | Description | Category | Amount
```

and calculate:

```text
Total Expenses
```

### SQLite GUI

Replace the CSV file with an SQLite database:

```text
SQLite Database
      ↓
    SQL
      ↓
 Python
      ↓
   Tkinter
      ↓
 Treeview Table
```

---

# 🛠️ Technologies Used

- **Python**
- **Tkinter**
- **Pandas**
- **CSV**
- **JSON**
- **datetime**
- **ttk.Treeview**

---

## 📌 Beginner Note

These applications intentionally use straightforward Python rather than advanced object-oriented programming, complex GUI frameworks, or external architectures.

The goal is to understand the basic relationship between:

```text
Python Code
    +
Data
    +
GUI
    =
Desktop Application
```

Once these fundamentals are comfortable, the applications can be extended with search, filtering, CRUD operations, SQLite, APIs, validation, error handling, and better GUI layouts.

---

## 👤 Author

**Rohan D** — Workforce Development Program Coordinator
Technical Instructor — IT Support · Web Development · Data Analytics · Databases · Programming

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/deshpande-rohan/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/Rohan-Repo)
![Updated](https://img.shields.io/badge/Updated-2026-brightgreen?style=plastic)
