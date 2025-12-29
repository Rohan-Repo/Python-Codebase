import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import os

def insert_name_into_pdf(template_pdf_path, output_pdf_path, name, x, y):
    # Read the original PDF
    reader = PdfReader(template_pdf_path)
    writer = PdfWriter()
    
    # Create a PDF to overlay with the new name
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Insert the name at the specified position
    can.drawString(x, y, name)
    can.showPage()
    
    can.save()
    
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    overlay_pdf = PdfReader(packet)
    
    # Merge the original PDF with the new overlay PDF
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        overlay_page = overlay_pdf.pages[0]
        page.merge_page(overlay_page)
        writer.add_page(page)
    
    # Write the updated PDF to a file
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

def process_csv_and_update_pdfs(csv_file_path, template_pdf_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Assuming the column with names is called 'Name'
    for index, row in df.iterrows():
        name = row['Names']
        output_pdf_path = os.path.join(os.path.dirname(csv_file_path), f'updated_{index + 1}.pdf')
        insert_name_into_pdf(template_pdf_path, output_pdf_path, name, 300, 300)
        break

# Example usage
csv_file_path = 'input.csv'  # Path to your CSV file
template_pdf_path = 'Cert-1.pdf'  # Path to your template PDF
process_csv_and_update_pdfs(csv_file_path, template_pdf_path)
