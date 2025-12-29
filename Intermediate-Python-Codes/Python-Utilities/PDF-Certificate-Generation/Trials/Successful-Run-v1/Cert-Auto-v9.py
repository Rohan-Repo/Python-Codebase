# Create a CSV file with the PPT Names under a "Names" column

# Install these Python Packages - 
# pip install pandas PyPDF2 reportlab
# pandas - To Read Data from CSV File 
# PyPDF2 reportlab - To Create and update PDF Files

import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
import io
import os

def insert_name_into_pdf(template_pdf_path, output_pdf_path, name, x, y, font_name='Helvetica', font_size=12, font_color=(0, 0, 0)):
    # Read the original PDF
    reader = PdfReader(template_pdf_path)
    writer = PdfWriter()
    
    # Create a PDF to overlay with the new name
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Set the font and color
    can.setFont(font_name, font_size)
    can.setFillColor(Color(*font_color))  # Color expects RGB tuple
    
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

    # Create a "Certificates" folder if it doesn't exist
    output_folder = os.path.join(os.path.dirname(csv_file_path), 'Certificates')
    os.makedirs(output_folder, exist_ok=True)

    # Assuming the column with names is called 'Name'
    for index, row in df.iterrows():
        name = row['Names']
        print( name, ' : ', len(name) )
        output_pdf_path = os.path.join(output_folder, f'{name}.pdf')

        # Update Font-Size, X & Y Co-ordinates based on length of name 
        if len(name) >= 18:
            insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 400, 300, font_name='Helvetica-Bold', font_size=17, font_color=(0.184, 0.31, 0.31) )  # steelblue color
        else:
            insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 425, 300, font_name='Helvetica-Bold', font_size=20, font_color=(0.184, 0.31, 0.31) )  # steelblue color

csv_file_path = 'input.csv'  # Path to your CSV file
# Export this Template PDF from Canva
template_pdf_path = 'templateCert.pdf'  # Path to your template PDF
process_csv_and_update_pdfs(csv_file_path, template_pdf_path)