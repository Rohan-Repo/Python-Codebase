# ☕ Coffee Shop EDA — Data Analysis with Python

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.x-4C72B0?style=flat)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=flat&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)

> A hands-on Exploratory Data Analysis (EDA) project built on coffee shop transaction data.
> Covers data loading, cleaning, statistical summaries, and **8 chart types** using
> **Matplotlib**, **Seaborn**, and **Plotly** — progressively across three notebooks.

---

## 📁 Repository Structure

```
coffee-shop-eda/
│
├── 📓 0-Coffee-Shop-EDA-Seaborn-Matplotlib.ipynb
│       └── Foundational EDA using Seaborn + Matplotlib with
│           chart-choice explanations and parameter comments
│
├── 📓 1-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-All.ipynb
│       └── All 3 libraries side-by-side for every chart type
│           (Matplotlib → Seaborn → Plotly per section)
│
├── 📓 2-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-Selective.ipynb
│       └── Best library selected per chart type, with a
│           chart-selection reference guide and EDA conclusions
│
├── 📄 coffee_shop_transactions_cleaned.csv
│       └── Pre-cleaned dataset — 21 transactions, 7 columns
│
└── 📄 README.md
```

---

## 📊 Dataset Overview

| Property | Value |
|---|---|
| **File** | `coffee_shop_transactions_cleaned.csv` |
| **Rows** | 21 transactions |
| **Columns** | 7 |
| **Date Range** | 1 September 2025 → 26 September 2025 |
| **Items Sold** | Americano, Bagel, Cappuccino, Croissant, Espresso, Latte, Mocha, Muffin, Tea |
| **Payment Methods** | Cash, Credit Card, Mobile Pay |
| **Total Revenue** | $105.60 |

### Columns

| Column | Type | Description |
|---|---|---|
| `TransactionID` | string | Unique ID for each transaction (e.g. TX1001) |
| `DateTime` | datetime64 | Date and time of the transaction |
| `Item` | string | Name of the item purchased |
| `PricePerItem` | float | Price of one unit of the item ($) |
| `Quantity` | integer | Number of units purchased |
| `TotalPrice` | float | PricePerItem × Quantity |
| `PaymentMethod` | string | How the customer paid |

---

## 📓 Notebook Guide

### `0-Coffee-Shop-EDA-Seaborn-Matplotlib.ipynb`
**Level:** Beginner → Intermediate

The foundation notebook. Starts with a clean dataset and walks through 9 EDA steps:

| # | Analysis | Method |
|---|---|---|
| 1 | Dataset Snapshot | `.describe()` `.nunique()` `.sum()` |
| 2 | Items Ordered | `value_counts()` → `sns.barplot` |
| 3 | Revenue by Item | `groupby` + `sum()` → `sns.barplot` (horizontal) |
| 4 | Payment Method Split | `value_counts()` → `axes[0].pie` + `sns.barplot` |
| 5 | Daily Revenue Trend | `.dt.date` + `groupby` → `sns.lineplot` |
| 6 | Busiest Hours | `.dt.hour` → `sns.countplot` |
| 7 | Order Value Distribution | `sns.histplot(kde=True)` + `sns.boxplot` |
| 8 | Correlation Heatmap | `.corr()` → `sns.heatmap(annot=True)` |
| 9 | Key Insights Summary | `groupby` + `idxmax()` |

**Features:**
- Every plot parameter has an inline comment explaining what it does
- Each chart section includes a markdown cell explaining **why that chart type was chosen**
- `parse_dates=['DateTime']` used at load time to avoid `.dt` accessor errors

---

### `1-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-All.ipynb`
**Level:** Intermediate

Covers all 8 chart types with **all three libraries shown side-by-side** for every chart.
Designed to teach the differences between libraries using the same dataset and question.

| # | Chart Type | Business Question |
|---|---|---|
| 1 | Bar Chart | Which items generate the most total revenue? |
| 2 | Horizontal Bar | Which items sold the most units? |
| 3 | Pie Chart | What share of revenue comes from each payment method? |
| 4 | Line Chart | How does daily revenue trend across the month? |
| 5 | Count Plot | How many transactions per payment method? |
| 6 | Histogram | What does the distribution of order amounts look like? |
| 7 | Box Plot | How does price vary across items? |
| 8 | Heatmap | How are numeric columns correlated? |

**Each section shows:**
```
Matplotlib  →  full manual control, most code
Seaborn     →  statistical defaults, cleaner syntax
Plotly      →  interactive (hover, zoom, download)
```

**Summary table at the end** maps each chart to its business question and key insight.

---

### `2-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-Selective.ipynb`
**Level:** Intermediate → Applied

The most strategic notebook. Picks the **best library per chart type** rather than showing all three.
Includes a chart-selection reference guide at the top.

**Chart Selection Reference (first cell):**

| Business Question | Best Chart | Why? |
|---|---|---|
| Compare category sizes | Bar Chart | Easy side-by-side comparison |
| Rank items | Horizontal Bar | Natural reading order (top to bottom) |
| Show part-to-whole | Pie Chart | Proportional slices sum to 100% |
| Track change over time | Line Chart | Connects ordered points to show trend |
| Count category frequency | Count Plot | Bars represent row counts directly |
| Show value distribution | Histogram | Groups values into frequency buckets |
| Show spread and outliers | Box Plot | IQR + whiskers expose data spread |
| Show variable relationships | Heatmap | Colour grid reveals correlations instantly |

**Library Selection Made:**

| # | Chart | Library Chosen | Reason |
|---|---|---|---|
| 1 | Bar Chart | Matplotlib | Maximum labelling control |
| 2 | Horizontal Bar | Matplotlib | Clean rank ordering |
| 3 | Pie Chart | Plotly | Interactive hover on slices |
| 4 | Line Chart | Plotly | Hover shows exact daily values |
| 5 | Count Plot | Seaborn | Built-in `countplot()` — no pre-aggregate |
| 6 | Histogram | Seaborn | `kde=True` adds smooth curve in one line |
| 7 | Box Plot | Plotly | Hover reveals min/median/max/outliers |
| 8 | Heatmap | Seaborn | `annot=True` prints values automatically |

---

## 🛠 Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| **Python** | 3.12 | Core language |
| **Pandas** | 2.x | Data loading, cleaning, groupby, aggregation |
| **NumPy** | 1.x | Numeric operations |
| **Matplotlib** | 3.x | Static charts with full manual control |
| **Seaborn** | 0.13.x | Statistical charts with clean defaults |
| **Plotly Express** | 5.x | Interactive charts (hover, zoom) |
| **Jupyter Notebook** | 7.x | Development and presentation environment |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Rohan-Repo/Python-Codebase.git

cd /Intermediate-Python-Codes/Data-Analysis-Machine-Deep-Learning/Exploratory-Data-Analysis/DataViz-Matplotlib-Seaborn-Plotly
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn plotly jupyter
```

### 3. Launch Jupyter

```bash
jupyter notebook
```

### 4. Run the notebooks in order

```
0-Coffee-Shop-EDA-Seaborn-Matplotlib.ipynb       ← Start here
1-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-All.ipynb
2-Coffee-Shop-EDA-Matplotlib-Seaborn-Plotly-Selective.ipynb
```

> **Note:** Run all cells from top to bottom in each notebook.
> The CSV file must be in the **same folder** as the notebooks.

---

## 📈 Key Findings

| Metric | Finding |
|---|---|
| 💰 **Total Revenue** | $105.60 across 21 transactions |
| 🥇 **Top Revenue Item** | Revealed in notebook — see Section 3 |
| 💳 **Top Payment Method** | Revealed in notebook — see Section 4 |
| 🕐 **Busiest Hour** | Revealed in notebook — see Section 6 |
| 📊 **Strongest Correlation** | `Quantity` ↔ `TotalPrice` (strong positive) |
| 📅 **Date Range** | 1 Sep 2025 → 26 Sep 2025 |

---

## 🧠 Concepts Covered

```
Data Loading          → pd.read_csv() with parse_dates
Data Inspection       → .info(), .describe(), .dtypes, .shape
DateTime Handling     → .dt.date, .dt.hour
Aggregation           → groupby(), sum(), mean(), count(), value_counts()
Statistical Summary   → .describe(), .corr(), idxmax()
Matplotlib            → plt.bar, plt.barh, plt.pie, plt.plot,
                        plt.hist, plt.boxplot, plt.imshow
Seaborn               → sns.barplot, sns.lineplot, sns.countplot,
                        sns.histplot (kde=True), sns.boxplot, sns.heatmap
Plotly Express        → px.bar, px.pie, px.line, px.histogram,
                        px.box, px.imshow
Chart Selection       → Choosing the right chart for each question
```

---

## 📋 requirements.txt

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.13
plotly>=5.0
jupyter>=7.0
ipykernel>=6.0
```

---

## 👤 Author

**Rohan D**
Technical Instructor — IT Support · Web Development · Data Analytics · Databases · Programming

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/deshpande-rohan/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/Rohan-Repo)

---

## 📄 License

This project is for educational purposes.
Dataset is synthetic — generated for teaching and demonstration only.

---