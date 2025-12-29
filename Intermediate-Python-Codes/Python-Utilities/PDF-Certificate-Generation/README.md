# 🎓 Automated Certificate Generator

This project provides a Python-based automation tool to generate personalized certificates in bulk. It reads names from a CSV file and overlays them onto a professional PDF template, specifically designed for the **Coding Fundamentals** course.

## 🚀 Features

* **Batch Generation**: Automatically create multiple certificates from a single CSV list.
* **Dynamic Sizing**: Adjusts font size and positioning based on name length to prevent text overflow.
* **Professional Design**: Uses high-quality PDF templates with custom colors (Aquamarine/Teal).
* **Automatic Organization**: Saves all generated files into a dedicated Certificates/ folder.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `Cert-Auto-v9.py` | The main Python script that executes the automation logic. |
| `PP-Names.csv` | The input data source containing a list of recipient names. |
| `Coding-Fundamentals-Cert.pdf` | The base certificate template (Background, Signatures, and Static Text). |
| `requirements.txt` | A list of necessary Python libraries (`pandas`, `PyPDF2`, `reportlab`). |
| `Certificates/` | *(Auto-generated)* The destination folder where finished PDFs are saved. |

---

## 🛠️ Setup & Installation

1.  **Prerequisites**: Ensure you have **Python 3.x** installed on your machine.
2.  **Install Dependencies**: Run the following command in your terminal/command prompt to install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

---

## 📑 Instructions

Follow these steps to generate your certificates:

### 1. Prepare the Data
Open `PP-Names.csv` and ensure it has a column header titled **Names**. Add the list of all recipients under this header.
* *Example: John Doe, Jane Doe, Mary Smith*

### 2. Template Placement
Ensure the file `Coding-Fundamentals-Cert.pdf` is located in the **root directory** of the project (the same folder as the script).
* *Note: This template can be generated via Canva or Gen AI*

### 3. Run the Script
Execute the automation script by running:

```bash
python Cert-Auto-v9.py
```

### 4. Retrieve Certificates
Once the script finishes, check the newly created `Certificates/` folder. You will find individual PDF files named after each recipient.