# pip install pymupdf
# pip install fitz

import csv
import fitz  # PyMuPDF
import os

# Function to read names from CSV file
def read_names_from_csv(csv_file):
    names = []
    with open(csv_file, mode='r', encoding='ISO-8859-1') as file:  # Use ISO-8859-1 encoding
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Ensure we handle each element as a string
            name = str(row).strip()
            names.append(name)
    return names

# Function to create a PDF with a given name at a specific position using fitz
def create_pdf(template_pdf, output_pdf, name, x, y):
    # Open the template PDF
    doc = fitz.open(template_pdf)
    
    # Select the first page
    page = doc
    
    # Set the font and size
    font_size = 12
    
    # Insert the text at the specified position
    page.insert_text((x, y), name, fontsize=font_size)
    
    # Save the new PDF
    doc.save(output_pdf)

# Main function to generate PDFs based on CSV input
def generate_pdfs(csv_file, template_pdf, x, y):
    names = read_names_from_csv(csv_file)
    for name in names:
        output_pdf = os.path.join(os.getcwd(), f"{name}.pdf")  # Save to the current working directory
        create_pdf(template_pdf, output_pdf, name, x, y)

# Example usage
csv_file = 'pp_names2.csv'  # Replace with your CSV file path
template_pdf = 'Cert-1.pdf'  # Replace with your template PDF file path
x_position = 100  # Replace with your desired x position
y_position = 150  # Replace with your desired y position
generate_pdfs(csv_file, template_pdf, x_position, y_position)
