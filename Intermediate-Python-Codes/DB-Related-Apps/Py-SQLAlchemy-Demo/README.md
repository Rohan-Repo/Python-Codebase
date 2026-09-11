# Python SQLAlchemy — Multi-Database Employee Viewer

A beginner-friendly Python project that demonstrates how to connect to **four different databases** (SQLite, MySQL, SQL Server and PostgreSQL) using **SQLAlchemy**, fetch data, and display it — both as a **CLI terminal output** and as a **Tkinter GUI grid**.

The project is split into two self-contained parts:

| Part | Folder | Interface |
|---|---|---|
| CLI | `Py-SQLAlchemy-Multiple-DBs-CLI` | Terminal / Command Line |
| GUI | `Py-SQLAlchemy-Multiple-DBs-TKinter-GUI` | Tkinter Desktop Window |

Each part is fully independent and contains its own `requirements.txt` and SQL setup scripts.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Database Setup](#database-setup)
- [Part 1 — CLI (Command Line)](#part-1--cli-command-line)
- [Part 2 — GUI (Tkinter)](#part-2--gui-tkinter)
- [Key Concepts Explained](#key-concepts-explained)
- [Requirements](#requirements)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Common Errors and Fixes](#common-errors-and-fixes)
- [Dataset Used](#dataset-used)
- [Technologies](#technologies)

---

## Project Overview

This project teaches how to use **SQLAlchemy** — Python's most popular database toolkit — to query a real database and work with the results. The same core query is implemented progressively across multiple files:

```
SELECT * FROM Employee ORDER BY empSalary DESC
```

Two approaches to handling results are demonstrated:

- **Normal Python Objects** — rows come back as ORM objects; access data with `emp.empFirstName`
- **Dataclasses** — rows are immediately converted into plain Python dataclasses; no live DB connection, easy to serialise

---

## Folder Structure

```
Py-SQLAlchemy-Demo/
│
├── Py-SQLAlchemy-Multiple-DBs-CLI/
│   ├── requirements.txt
│   ├── SQL-DB-Creation/
│   │   ├── Employee-Table-Creation-SQLServer.sql
│   │   ├── Employee-Table-Creation-MySQL.sql
│   │   ├── Employee-Table-Creation-PostgreSQL.sql
│   │   └── Employee-Table-Creation-SQLite.sql
│   │
│   └── DB-Wise-Codes/
│       ├── SQLite/
│       │   └── query_sqlite.py                  ← SQLite only, simplest starting point
│       │
│       ├── MySQL-SQLite/
│       │   └── query_sqlite_mysql.py            ← MySQL + SQLite, single file
│       │
│       ├── MySQL-SQLServer-SQLite/
│       │   ├── database_MS_SS_S.py              ← connection menu (3 DBs)
│       │   ├── query_normal_MS_SS_S.py          ← ORM objects approach
│       │   └── query_dataclass_MS_SS_S.py       ← dataclass approach
│       │
│       └── MySQL-SQLServer-SQLite-PostgreSQL/
│           ├── connectToDB.py                   ← connection menu (all 4 DBs)
│           ├── query_normal.py                  ← ORM objects approach
│           └── query_dataclass.py               ← dataclass approach
│
└── Py-SQLAlchemy-Multiple-DBs-TKinter-GUI/
    ├── requirements.txt
    ├── SQL-DB-Creation/
    │   └── (same 4 SQL files as above)
    │
    ├── GUI-Normal-Code/
    │   ├── gui_grid_sqlite_mysql.py             ← single-file GUI (SQLite + MySQL)
    │   └── gui_grid_all_DBs.py                  ← single-file GUI (all 4 DBs)
    │
    └── GUI-MVC-Code/
        ├── model.py                             ← M: table structure
        ├── database.py                          ← DB connectivity layer
        ├── controller.py                        ← C: bridge between GUI and DB
        └── view.py                              ← V: Tkinter window — run this
```

---

## Database Setup

Run the appropriate SQL script in your database tool **before** running any Python file. Each script creates the `CompanyDatabase`, the `Employee` table, and inserts sample data.

| Database | Script | Tool |
|---|---|---|
| SQL Server | `Employee-Table-Creation-SQLServer.sql` | SSMS |
| MySQL | `Employee-Table-Creation-MySQL.sql` | MySQL Workbench |
| PostgreSQL | `Employee-Table-Creation-PostgreSQL.sql` | pgAdmin / psql |
| SQLite | `Employee-Table-Creation-SQLite.sql` | DB Browser for SQLite |

> **SQLite only:** The `.db` file (`EmpDB.db`) is already included in each folder. No SQL script needs to be run — it is ready to use immediately.

### Employee Table Schema

```sql
CREATE TABLE Employee (
    empId        INT PRIMARY KEY,   -- auto-incremented ID
    empFirstName VARCHAR(30),
    empLastName  VARCHAR(30),
    empSalary    INT NOT NULL CHECK (empSalary > 20000),
    empCity      VARCHAR(50) NOT NULL,
    empCountry   VARCHAR(50) NOT NULL
);
```

### ID Starting Points

Each database uses a different auto-increment starting value to make it easy to identify the source at a glance:

| Database | ID starts at |
|---|---|
| SQL Server | 100 |
| MySQL | 200 |
| PostgreSQL | 300 |
| SQLite | 1 |

### Sample Data

| Database | Dataset |
|---|---|
| SQL Server | Harry Potter cast — cities in UK, Sweden, Germany, Oman, UAE |
| MySQL | Friends cast — cities in Germany, Canada, India, UAE |
| PostgreSQL | Suits cast — cities in Greece, Poland, Philippines |
| SQLite | Generic names — cities in India, Canada, KSA |

---

## Part 1 — CLI (Command Line)

All CLI scripts print a formatted employee table to the terminal, sorted by salary highest first. Navigate to the folder of the script you want to run and execute it.

### SQLite only (simplest)

```bash
cd Py-SQLAlchemy-Multiple-DBs-CLI/DB-Wise-Codes/SQLite
python query_sqlite.py
```

No menu — connects to `EmpDB.db` immediately. Best starting point for beginners.

---

### MySQL + SQLite

```bash
cd Py-SQLAlchemy-Multiple-DBs-CLI/DB-Wise-Codes/MySQL-SQLite
python query_sqlite_mysql.py
```

Prompts:
```
Pick a database:
1. MySQL
2. SQLite
Enter 1 or 2:
```

---

### MySQL + SQL Server + SQLite

Two scripts share a common `database_MS_SS_S.py` which handles the connection menu.

```bash
cd Py-SQLAlchemy-Multiple-DBs-CLI/DB-Wise-Codes/MySQL-SQLServer-SQLite

# ORM objects approach
python query_normal_MS_SS_S.py

# Dataclass approach
python query_dataclass_MS_SS_S.py
```

Prompts:
```
Pick a database:
1. MySQL
2. SQL Server
3. SQLite
Enter 1, 2 or 3:
```

---

### All 4 Databases (MySQL + SQL Server + PostgreSQL + SQLite)

Two scripts share `connectToDB.py` which handles all four connections.

```bash
cd Py-SQLAlchemy-Multiple-DBs-CLI/DB-Wise-Codes/MySQL-SQLServer-SQLite-PostgreSQL

# ORM objects approach
python query_normal.py

# Dataclass approach
python query_dataclass.py
```

Prompts:
```
Pick a database:
1. MySQL
2. SQL Server
3. PostgreSQL
4. SQLite
Enter 1, 2, 3 or 4:
```

---

### CLI Sample Output

```
ID    First Name   Last Name        Salary   City             Country
-----------------------------------------------------------------
300   Harvey       Specter       $100,000   Athens           Greece
301   Jessica      Pearson        $95,000   Gdansk           Poland
302   Samantha     Wheeler        $88,000   Quezon City      Philippines
...

Total employees: 12
```

---

## Part 2 — GUI (Tkinter)

All GUI scripts open a desktop window with a radio button selector and a data grid. No terminal needed after launching.

### Normal Code (single file, no MVC)

```bash
cd Py-SQLAlchemy-Multiple-DBs-TKinter-GUI/GUI-Normal-Code

# SQLite + MySQL only
python gui_grid_sqlite_mysql.py

# All 4 databases
python gui_grid_all_DBs.py
```

### MVC Code (recommended)

```bash
cd Py-SQLAlchemy-Multiple-DBs-TKinter-GUI/GUI-MVC-Code
python view.py
```

The window shows four radio buttons — **SQLite · MySQL · SQL Server · PostgreSQL** — and a blue **Load Data** button. Select a database, click the button, and the grid populates instantly.

### MVC File Responsibilities

| File | Role | What it does |
|---|---|---|
| `model.py` | **M**odel | Describes the Employee table structure — two versions, one for PostgreSQL (lowercase columns) and one for all others |
| `database.py` | Connectivity | Stores all four connection strings; provides `get_engine()` and `is_postgresql()` |
| `controller.py` | **C**ontroller | Bridge between view and database — runs the query and returns results |
| `view.py` | **V**iew | Builds the Tkinter window — **only file you run** |

The MVC rule: `view.py` **never** imports from `database.py` or `model.py` directly. All data flows through `controller.py`. This means the GUI and the database are completely decoupled — you can swap one without touching the other.

---

## Key Concepts Explained

### SQLAlchemy Engine

```python
engine = create_engine("sqlite:///EmpDB.db")
```

The engine is the connection to the database. It prepares the connection but does **not** open it until a `Session` is started.

### Connection String Format

```
dialect+driver://username:password@host/database_name

sqlite:///EmpDB.db                                          ← SQLite (local file)
mysql+pymysql://compdbadmin:compdbadmin@localhost/CompanyDatabase
mssql+pyodbc://localhost/CompanyDatabase?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
postgresql+psycopg2://compdbadmin:compdbadmin@localhost/companydatabase
```

### ORM Model

```python
class Employee(Base):
    __tablename__ = "Employee"
    empId        = Column("empId",        Integer, primary_key=True)
    empFirstName = Column("empFirstName", String(30))
    empSalary    = Column("empSalary",    Integer)
    ...
```

Tells SQLAlchemy what the table looks like so it can build the right SQL.

### The Query

```python
with Session(engine) as session:
    employees = session.query(Employee).order_by(Employee.empSalary.desc()).all()
```

Python equivalent of `SELECT * FROM Employee ORDER BY empSalary DESC`.

### Normal Objects vs Dataclasses

```python
# Normal ORM object — still linked to SQLAlchemy
emp.empFirstName     # dot notation access

# Dataclass — plain Python, no DB connection
@dataclass
class EmployeeRecord:
    empId        : int
    empFirstName : str
    empSalary    : int
    ...

# Convert ORM → dataclass
record = EmployeeRecord(empId=row.empId, empFirstName=row.empFirstName, ...)

# Dataclass extras
dataclasses.asdict(record)   # → {"empId": 300, "empFirstName": "Harvey", ...}
record1 == record2           # equality comparison works automatically
```

### PostgreSQL Column Casing

PostgreSQL lowercases all names at storage time. `"empId"` becomes `"empid"`. The fix used throughout this project is a dedicated model:

```python
class EmployeePG(Base):
    __tablename__ = "employee"              # lowercase
    empId = Column("empid", Integer, ...)   # lowercase DB name, same Python attribute
```

---

## Requirements

```
sqlalchemy        # core ORM and connection toolkit
pymysql           # MySQL driver
pyodbc            # SQL Server driver
psycopg2-binary   # PostgreSQL driver
# SQLite — built into Python, no install needed
# tkinter — built into Python, no install needed
```

Install everything at once:

```bash
pip install -r requirements.txt
```

### Driver Prerequisites

| Database | Extra requirement |
|---|---|
| SQL Server | [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) |
| MySQL | None beyond `pymysql` |
| PostgreSQL | None beyond `psycopg2-binary` |
| SQLite | Nothing — ships with Python |

---

## Virtual Environment Setup

It is strongly recommended to use a virtual environment so libraries stay isolated to this project.

```bash
# Step 1 — Create the virtual environment (once only)
python -m venv .venv

# Step 2 — Activate it (every time you open a new terminal)
.venv\Scripts\activate        # Windows Command Prompt
.venv\Scripts\Activate.ps1   # Windows PowerShell
source .venv/bin/activate     # Mac / Linux

# You will see (.venv) at the start of your prompt when it is active

# Step 3 — Install dependencies (once only, after first activation)
pip install -r requirements.txt

# Step 4 — Run the code
python query_sqlite.py          # CLI example
python view.py                  # GUI example

# Step 5 — Deactivate when done
deactivate
```

---

## Common Errors and Fixes

### `relation "Employee" does not exist` (PostgreSQL)

PostgreSQL lowercases all names. The table is stored as `employee`, not `Employee`. Use `EmployeePG` model (already handled in all scripts) and ensure the `search_path` is set correctly.

### `permission denied for table employee` (PostgreSQL)

The user lacks SELECT permission. Run in psql or pgAdmin:

```sql
GRANT USAGE ON SCHEMA public TO compdbadmin;
GRANT SELECT ON TABLE public.employee TO compdbadmin;
```

### `Invalid column name 'empCountry'` (SQL Server)

Ensure you are using the `Employee` model (mixed-case columns), not the `EmployeePG` model. SQL Server preserves the original column casing.

### `Can't connect to MySQL server`

Check that MySQL is running and the credentials in the connection string match:

```python
"mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/YOUR_DATABASE"
```

### `pyodbc.InterfaceError` (SQL Server)

Ensure **ODBC Driver 17 for SQL Server** is installed on your machine. Download from the Microsoft link above.

---

## Dataset Used

The Employee table is populated with fictional characters from popular TV shows, mapped to real cities, to make the data memorable for learning purposes.

| Source | Characters | Cities |
|---|---|---|
| Harry Potter | Dumbledore, Snape, Granger, Weasley, Hagrid, Potter, Longbottom | London, Wembley, Stockholm, Malmo, Munich, Muscat, Abu Dhabi |
| Friends | Bing, Tribbiani, Greene, Buffay, Geller, Hosenstein, Central Perk | Berlin, Toronto, Vancouver, Calgary, Munich, Delhi, Dubai |
| Suits | Specter, Ross, Paulsen, Litt, Zane, Pearson, Bennett, Wheeler | Athens, Thessaloniki, Patras, Warsaw, Krakow, Gdansk, Manila, Cebu City |
| Generic | Stine, Doe, Smith, Walker, West, King | Mumbai, Toronto, Vancouver, Calgary, Kolkata, Delhi, Riyadh |

---

## Technologies

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Core language |
| SQLAlchemy | 2.x | ORM and database abstraction |
| tkinter | Built-in | Desktop GUI |
| SQLite | Built-in | Serverless local database |
| MySQL | 8.x | Relational database server |
| SQL Server | 2019+ | Microsoft relational database |
| PostgreSQL | 15+ | Open-source relational database |
| pymysql | Latest | Python driver for MySQL |
| pyodbc | Latest | Python driver for SQL Server |
| psycopg2-binary | Latest | Python driver for PostgreSQL |

---

## 👤 Author

**Rohan D** — Workforce Development Program Coordinator
Technical Instructor — IT Support · Web Development · Data Analytics · Databases · Programming

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/deshpande-rohan/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/Rohan-Repo)
![Updated](https://img.shields.io/badge/Updated-2026-brightgreen?style=plastic)
