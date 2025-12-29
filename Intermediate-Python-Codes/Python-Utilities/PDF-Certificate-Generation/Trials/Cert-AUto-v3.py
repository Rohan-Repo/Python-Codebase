import csv
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
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

# Function to create a PDF with a given name at a specific position
def create_pdf(template_pdf, output_pdf, name, x, y):
    # Create a temporary PDF with the name
    temp_pdf = "temp.pdf"
    c = canvas.Canvas(temp_pdf, pagesize=letter)
    c.drawString(x, y, name)
    c.save()

    # Read the template PDF
    reader = PdfReader(template_pdf)
    writer = PdfWriter()

    # Merge the temporary PDF with the template PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        if page_num == 0:
            # Merge the first page with the name
            temp_reader = PdfReader(temp_pdf)
            temp_page = temp_reader.pages
            page.merge_page(temp_page)
        writer.add_page(page)

    # Save the new PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

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
