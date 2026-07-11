# 🐍 Python Codebase

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=flat)

> A curated collection of Python scripts and Jupyter Notebooks covering everything from core language fundamentals to Machine Learning, Web Development, Database connectivity, and Data Analysis — built and maintained as part of teaching and continuous learning.

---

## 📋 Table of Contents

- [About](#about)
- [Installing Python](#installing-python)
- [Repository Structure](#repository-structure)
- [Section 1 — Base Python Codebases](#section-1--base-python-codebases)
- [Section 2 — Bootcamp Codebases](#section-2--bootcamp-codebases)
- [Section 3 — Intermediate Python Codes](#section-3--intermediate-python-codes)
- [Topics Covered](#topics-covered)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Author](#author)
- [License](#license)

---

## About

This repository provides practical Python examples, tutorials, and projects across a wide range of topics. It is designed for:

- **Beginners** learning Python syntax and core concepts
- **Intermediate developers** exploring data analysis, web development, and automation
- **Students** working through structured bootcamp curricula
- **Instructors** looking for reusable teaching materials

> Special thanks to [WikiHow](https://www.wikihow.com/Install-Python) and the [CanadianCoding YouTube channel](https://www.youtube.com/@canadiancoding) for foundational install and learning resources.

---

## Installing Python

| Platform | Resource |
|---|---|
| All platforms (guide) | [How to Install Python — WikiHow](https://www.wikihow.com/Install-Python) |
| macOS (video) | [Install Python on MacOS — YouTube](https://www.youtube.com/watch?v=3-sPfR4JEQ8) |
| Windows (video) | [Install Python on Windows — YouTube](https://www.youtube.com/watch?v=s6X_BVfncOw) |
| Official docs | [Python 3 Tutorial — docs.python.org](https://docs.python.org/3/tutorial/index.html) |
| CS50 Python (Part 1) | [YouTube](https://www.youtube.com/watch?v=0eNc5lJfZFM) |
| CS50 Python (Part 2) | [YouTube](https://www.youtube.com/watch?v=mgBpcQRDtl0) |

---

## Repository Structure

```
Python-Codebase/
│
├── 📁 Base-Python-Codebases/              ← Core Python fundamentals & classroom demos
│   ├── 📁 CS50-Python-Codes/              ← CS50P problem sets
│   ├── 📁 NP-Python-Demo-Files/           ← Classroom scripts & notebooks
│   ├── 📁 TC-SC-Python-Codes/             ← DSA, algorithms, OOP
│   └── 📁 python-rock-paper-scissors/     ← Mini CLI game
│
├── 📁 Bootcamp-Codebases/                 ← Structured bootcamp curriculum codebases
│   ├── 📁 CanTek-Python-Week-Codebase/    ← Python + SQL + Web Scraping assignments
│   ├── 📁 CodeWithHarry-Python-100-Days/  ← 100 Days of Code (day-by-day)
│   ├── 📁 LetsUpgrade-AI-ML-Batch-Codes/  ← AI/ML bootcamp (Day 3–14)
│   └── 📁 NP-Codebase/                    ← EDA, ML, NumPy, Pandas, Web Scraping
│
├── 📁 Intermediate-Python-Codes/          ← Applied intermediate-level code
│   ├── 📁 DB-Related-Apps/                ← MySQL CRUD with Python
│   ├── 📁 Data-Analysis-Machine-Deep-Learning/ ← EDA, ML, Plotly, SQL+Pandas
│   ├── 📁 Intermediate-Python-Concepts/   ← DataClasses, Logging Module
│   ├── 📁 Python-Utilities/               ← Email, QR codes, currency, file tools
│   └── 📁 Web-Dev-Related/                ← Flask apps + Django/DRF codebase
│
├── 📄 LICENSE                             ← GPL-3.0
└── 📄 README.md
```

---

## Section 1 — Base Python Codebases

### 📁 CS50-Python-Codes

Problem set solutions from [Harvard's CS50P](https://cs50.harvard.edu/python/).

| Folder | Files | Concepts |
|---|---|---|
| `01-Functions-Variables/` | `einstein.py` `faces.py` `indoor.py` `playback.py` `tip.py` | Functions, string formatting, type conversion |
| `02-Conditionals/` | `bank.py` `deep-thought.py` `file-extensions.py` `math-interpreter.py` `meal-time-*.py` | if/elif/else, match-case, input validation |
| `File-Handling/` | `simple_file_handling.py` `file_handling_with.py` `file_handling_with_errors.py` | open(), with statement, exception handling |
| Root | `print-dataTypes-loops.py` `python-data-structures.py` | Data types, loops, lists, dicts, sets |

---

### 📁 NP-Python-Demo-Files

Classroom demonstration files includes multilingual Hello World examples and core Python concepts.

```
HelloWorld-Codes/
  Codes/         ← Hello World in C, C++, HTML, Java, Python
  Screenshots/   ← Screenshots for classroom slide use

Python Scripts:
  ClassEg.py                           ← Classes and OOP
  ExceptionHandling.py / 2.py          ← try/except/finally, custom exceptions
  GrabURLData.py                        ← HTTP requests
  HashesDemo.py                         ← Hashing in Python
  Num-Arith-Operations.py               ← Arithmetic operators
  Py-Conditionals-Loops.py             ← if/elif, for, while
  Py-Data-Structures.py / -2.py        ← Lists, tuples, sets, dicts
  Py-Functions-Conditionals-Loops.py   ← Combined demo
  Py-QueueWithList.py                   ← Queue with list
  Py-StackWithList.py                   ← Stack with list
  Py-Variable-Arith.py                  ← Variables and arithmetic
  RandomNums.py                         ← random module
  StringMethods.py                      ← String operations
  UniqueSetValues.py                    ← Sets and deduplication

Notebooks:
  Python-Fundamentals-Codebase.ipynb   ← Complete fundamentals walkthrough
  Queue-Using-Dequeue.ipynb            ← collections.deque
```

---

### 📁 TC-SC-Python-Codes

Algorithms, Data Structures, and OOP exercises.

| Category | Files |
|---|---|
| **Search Algorithms** | `LinearSearch.py` `BinarySearch.py` `Search_With_BST_Implementation.py` |
| **Binary Search Trees** | `BinarySearchTree-1.py` → `BinarySearchTree-5.py` `Tree.py` |
| **OOP** | `OOPSEg.py` `OOPSEg2.py` `Phonebook.py` |
| **Data Structures** | `Py-Lists.py` `Py-Dicts.py` `List-Advanced.py` |
| **Control Flow** | `Py-Intro.py` `Py-Loops.py` `Py-Functions.py` `Py-Decision-Conditionals.py` |
| **Problem Sets** | `Py-Intro-Problems.py` `Py-Functions-Problems.py` `Py-Decision-Conditionals-Problems.py` |
| **Utilities** | `Py-DateTimeZones.py` `RandomNums.py` `StringMethods.py` `CreateQRCode.py` |

---

### 📁 python-rock-paper-scissors

`RPS.py` — A fully interactive command-line Rock, Paper, Scissors game demonstrating conditionals, functions, user input, and game loop logic.

---

## Section 2 — Bootcamp Codebases

### 📁 CanTek-Python-Week-Codebase

Structured week-long Python bootcamp with practice notebooks and graded assignments.

```
Python-Practice-Codes/
  Python-Basics.ipynb              ← Variables, types, input/output
  Day_1_Python_practice.ipynb      ← Hands-on exercises
  Numpy-Pandas-Crash-Course.ipynb  ← NumPy arrays + Pandas DataFrames
  PostGreSQL-Conn.ipynb            ← PostgreSQL connectivity

Python-SQL-Assg-3/
  CanTek-Py-Assg-3-Notebook.ipynb  ← Python + SQL assignment
  CanTek-Py-Assg-3-Queries.sql     ← SQL queries

Python-Web-Scraping-Assg-4/
  Python-Web-Scraping-v6.ipynb     ← Final web scraping solution
  Python-Jobs-API/
    Python-Jobs-API-v2.ipynb       ← Job listings API (multiple versions)
    JSON-Data/                     ← Scraped jobs (Data Analyst, FSD, Python Dev)
```

---

### 📁 CodeWithHarry — Python 100 Days of Code

Day-by-day Python learning following the [CodeWithHarry 100 Days curriculum](https://www.youtube.com/@CodeWithHarry).

| Days | Topic |
|---|---|
| 01–04 | Python basics, scripts |
| 05 | Comments and escape sequences |
| 06 | Variables and data types |
| 09 | Type casting |
| 11–12 | Strings and string slicing |
| 13 | Conditionals |
| 16 | Match-case (Python 3.10+) |
| 17–18–19 | Loops (for, while) |
| 22–23 | Lists |

**Mini Projects:**
```
Calculator/                    ← Arithmetic calculator
Greetings/                     ← Personalised greeting generator
Grocery-Bill-Shipping-Costs/   ← Bill + shipping cost logic
```

---

### 📁 LetsUpgrade AI/ML Batch Codes

Assignments from the **LetsUpgrade AI/ML Bootcamp**.

| Day | Notebook | Focus |
|---|---|---|
| Day 03 | `LU-Python-Assg-Day-3.ipynb` | Python fundamentals |
| Day 04 | `LU-Python-Assg-Day-4.ipynb` | Data types and structures |
| Day 05 | `LU-Python-Assg-Day-5.ipynb` | Functions and control flow |
| Day 06 | `LU-Python-Assg-Day-6.ipynb` | OOP basics |
| Day 07 | `LU-EDA-Assg-Day-7.ipynb` | Intro to EDA |
| Day 10 | `LU-EDA-Assg-Day-10.ipynb` | Attrition hypothesis analysis |
| Day 14 | `RD-Numpy Assignment-LU.ipynb` | NumPy arrays |

---

### 📁 NP-Codebase

#### 📊 EDA
```
Coffee-Shop-EDA-Seaborn-Matplotlib-2.ipynb  ← EDA with dark theme
coffee_shop_transactions_cleaned.csv        ← Dataset (21 rows, 7 columns)
Coffee-Shop-EDA-Charts-1.jpg / -2.jpg      ← Chart preview images
requirements.txt
```

#### 🤖 Machine Learning
```
LinearRegression-California-1.ipynb    ← California Housing regression
LinearRegression-California-2.ipynb    ← Extended analysis
LinearRegression-HousePrice.ipynb      ← House price prediction
CustomerSegmentation-KMeans.ipynb      ← K-Means customer clustering
California_Housing_Data.csv
Created_Housing_Data.csv
Customer_Data.csv
```

#### 🐍 Python Language Fundamentals
```
00-Python-Fundamentals.ipynb            ← Complete fundamentals notebook
01-PY-Day-1.ipynb                       ← Print, variables, data types
02-PY-Day-2.ipynb                       ← Conditions, loops, functions
03-PY-Day-3.ipynb                       ← OOP, file handling, modules
CreateQRCode.ipynb                      ← QR code generation
Queue-Using-Dequeue.ipynb               ← collections.deque
Stack-Queue-Using-List.ipynb            ← Stack and queue with lists
RandomNumbers-NumberFunctions.ipynb     ← random + math modules
greetUser.ipynb                         ← Input/output starter exercise
File-Handling/                          ← Read, write, append examples
```

#### 🌐 Python Web Scraping
```
GrabURLData.ipynb          ← Fetching data with requests
Web-Scraping-Demo-2.ipynb  ← BeautifulSoup HTML scraping
```

---

## Section 3 — Intermediate Python Codes

### 🗄️ DB-Related-Apps / MySQL

```
Python MySQL DB CRUD Operations.ipynb
  └── Full Create, Read, Update, Delete with mysql-connector-python
      Table creation, INSERT, SELECT, UPDATE, DELETE, parameterised queries
```

---

### 📊 Data Analysis, Machine Learning & Deep Learning

#### Exploratory Data Analysis — DataViz (Matplotlib / Seaborn / Plotly)

```
0-Coffee-Shop-EDA-Seaborn-Matplotlib.ipynb
  └── 9 EDA steps with chart-choice explanations and inline parameter comments
      Charts: bar, horizontal bar, pie, line, countplot, histplot, boxplot, heatmap

1-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-All.ipynb
  └── All 8 chart types — Matplotlib, Seaborn, and Plotly shown side-by-side
      for every chart type on the same dataset

2-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-Selective.ipynb
  └── Chart-selection reference guide (best library per chart type)
      Full EDA conclusions and business insights summary table

coffee_shop_transactions_cleaned.csv  ← 21 transactions, 7 columns
requirements.txt
```

| Chart | Matplotlib | Seaborn | Plotly |
|---|---|---|---|
| Bar | `plt.bar` | `sns.barplot` | `px.bar` |
| Horizontal Bar | `plt.barh` | `sns.barplot` | `px.bar(orientation='h')` |
| Pie | `plt.pie` | via matplotlib | `px.pie` |
| Line | `plt.plot` | `sns.lineplot` | `px.line` |
| Count | `plt.bar` (manual) | `sns.countplot` | `px.histogram` |
| Histogram | `plt.hist` | `sns.histplot(kde=True)` | `px.histogram` |
| Box | `plt.boxplot` | `sns.boxplot` | `px.box` |
| Heatmap | `plt.imshow` | `sns.heatmap(annot=True)` | `px.imshow` |

#### Numpy Tutorial
```
Numpy-Tut.ipynb  ← Arrays, indexing, slicing, broadcasting,
                   aggregation functions, linear algebra
```

#### Pandas Tutorial
```
KG-Pandas-Practice.ipynb  ← DataFrame creation, data cleaning,
                             filtering, groupby, merge, pivot tables
```

#### SQL Joins + Pandas Merge / Concat / Join
```
SQLJoins-Pandas-Merge-Concat-Join.ipynb
  └── Side-by-side: SQL JOINs vs Pandas merge(), concat(), join()
      INNER, LEFT, RIGHT, FULL OUTER joins demonstrated in both
DB-Insert-SQLJoins.sql  ← SQL script with sample product data
```

#### Machine Learning
```
Spotify - Decision Tree & Random Forest - Version 1.0.ipynb
  └── Classification on Spotify track data
      Decision Tree → Random Forest comparison
      Feature importance, confusion matrix, accuracy metrics
```

---

### 🧠 Intermediate Python Concepts

#### Python DataClasses
```
Py-DataClasses.ipynb
  └── @dataclass decorator, field() with defaults,
      __post_init__(), frozen=True, inheritance,
      __eq__, __lt__ with order=True
```

#### Python Logging Module
```
Py-Logging-RootLogger.ipynb
  └── Root logger, log levels (DEBUG/INFO/WARNING/ERROR/CRITICAL),
      StreamHandler, FileHandler, Formatter

Py-Logging-CustomLogger.ipynb
  └── Named loggers, RotatingFileHandler, TimedRotatingFileHandler,
      custom log formats, multiple handlers on one logger

logs/  ← Sample output log files
```

---

### 🔧 Python Utilities

| Utility | File(s) | What It Does |
|---|---|---|
| **Append DOCX Files** | `append-multiple-docx-files.py` | Merge multiple Word documents into one using python-docx |
| **Currency Exchange** | `GetAllSymbols.py` `GetLatestRates.py` | Live exchange rates via Frankfurter / Open Exchange API |
| **Find Duplicates** | `findDuplicatesInTextFile.py` | Detect and report duplicate lines in text files |
| **QR Code Generator** | `Generate-QR-Code.py` | Generate QR codes from URLs or text with qrcode library |
| **Date & Time** | `Date-Time.py` | datetime formatting, timezone handling, timedelta arithmetic |
| **Text to Speech** | `Py-Text-To-Speech.py` | Convert text to audio using pyttsx3 |
| **CSV Reader** | `Read-CSV-File.py` | Read and process CSV data with csv module |
| **JSON Reader** | `Read-JSON-File.py` `Read-Multiple-JSON-Files.py` | Parse single and batch JSON files |
| **Crypto Demo** | `CryptoEg.py` | Symmetric encryption basics with the cryptography library |
| **Random Text** | `GenerateRandomText.py` | Generate random placeholder text |
| **Send Email** | `sendEmail.py` `sendEmail-OTP.py` | Send emails and OTPs via smtplib + SMTP |

---

### 🌐 Web Development

#### Flask Framework — 4 Applications

| App | Folder | Key Features |
|---|---|---|
| **CS50 Flask** | `CS50/` | Jinja2 templates, routes, form handling |
| **Company Dashboard** | `Company-Dashboard-App/` | Multi-page dashboard with static resources |
| **Display DB Data** | `Display-DB-Data-Flask/` | Reads from SQL DB, renders data in HTML tables |
| **Frosh IMs** | `Frosh-IMs/` | Sports intramural registration (CS50W problem set) |

All Flask apps use:
```
app.py         ← Routes, view functions, Flask app instance
templates/     ← Jinja2 HTML templates (extend base layout)
static/        ← CSS, images (where applicable)
```

#### Django + Django REST Framework
```
Django-DjangoRestAPI-Codebase/
  └── Django web app + REST API endpoints
      Django models, views, serializers (DRF)
      CRUD API with JSON responses
```

---

## Topics Covered

```
Python Fundamentals     Variables, data types, operators, input/output
Control Flow            if/elif/else, match-case, for, while loops
Functions               def, *args, **kwargs, lambda, scope, recursion
Data Structures         Lists, tuples, sets, dicts, deque, stacks, queues
OOP                     Classes, objects, inheritance, encapsulation
Exception Handling      try/except/finally, custom exceptions
File Handling           open(), read(), write(), with statement, csv, json
Algorithms              Linear search, binary search, BST, sorting
NumPy                   Arrays, indexing, broadcasting, linear algebra
Pandas                  DataFrames, cleaning, groupby, merge, pivot tables
Matplotlib              Bar, line, pie, histogram, box, heatmap (static)
Seaborn                 barplot, lineplot, countplot, histplot, heatmap
Plotly                  Interactive charts — hover, zoom, drill-down
EDA                     Statistical summary, distributions, correlations
Machine Learning        Linear regression, decision tree, random forest, K-Means
Web Scraping            requests, BeautifulSoup, JSON APIs, urllib
Flask                   Routes, Jinja2 templates, forms, static files
Django                  Models, views, templates, ORM, REST API (DRF)
MySQL                   CRUD operations with mysql-connector-python
PostgreSQL              Connection and queries with psycopg2
Intermediate Concepts   DataClasses, logging module, datetime, cryptography
Python Utilities        Email (SMTP), QR codes, text-to-speech, file tools
```

---

## Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.12 |
| **Notebooks** | Jupyter Notebook / JupyterLab |
| **Data Analysis** | Pandas, NumPy |
| **Visualisation** | Matplotlib, Seaborn, Plotly Express |
| **Machine Learning** | scikit-learn |
| **Web Framework** | Flask, Django, Django REST Framework |
| **Databases** | MySQL, PostgreSQL, SQLite |
| **Web Scraping** | requests, BeautifulSoup4, urllib |
| **Utilities** | pyttsx3, qrcode, cryptography, python-docx |
| **Dev Tools** | Git, GitHub, VS Code, PyCharm |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Rohan-Repo/Python-Codebase.git
cd Python-Codebase
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Sub-folders with their own `requirements.txt` should be installed individually.

### 3. Launch Jupyter for notebooks

```bash
jupyter notebook
```

### 4. Run Python scripts

```bash
python Base-Python-Codebases/TC-SC-Python-Codes/BinarySearch.py
python Intermediate-Python-Codes/Python-Utilities/Misc-Utils/Generate-QR-Code.py
```

### 5. Run Flask apps

```bash
cd Intermediate-Python-Codes/Web-Dev-Related/Flask-Framework/Company-Dashboard-App
python app.py
# Open http://127.0.0.1:5000 in your browser
```

---

## Official Resources

| Resource | Link |
|---|---|
| Python Docs | [docs.python.org](https://docs.python.org/3/tutorial/index.html) |
| CS50 Python | [cs50.harvard.edu/python](https://cs50.harvard.edu/python/) |
| Pandas Docs | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| NumPy Docs | [numpy.org/doc](https://numpy.org/doc/) |
| Seaborn Docs | [seaborn.pydata.org](https://seaborn.pydata.org/) |
| Plotly Docs | [plotly.com/python](https://plotly.com/python/) |
| Flask Docs | [flask.palletsprojects.com](https://flask.palletsprojects.com/) |
| Django Docs | [docs.djangoproject.com](https://docs.djangoproject.com/) |
| scikit-learn | [scikit-learn.org](https://scikit-learn.org/stable/) |

---

## Author

**Rohan Deshpande**
Technical Instructor — IT Support · Web Development · Data Analytics · Databases · Programming · System Administration · Scripting

> *Ask me about Java, Spring, Angular, Python, SQL, PowerShell, and Shell Scripting.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deshpande-rohan/)
[![GitHub](https://img.shields.io/badge/GitHub-Rohan--Repo-181717?style=flat&logo=github&logoColor=white)](https://github.com/Rohan-Repo)

---

## License

This repository is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](LICENSE) file for full details.

---
