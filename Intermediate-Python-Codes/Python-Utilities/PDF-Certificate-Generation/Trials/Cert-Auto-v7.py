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

    # Assuming the column with names is called 'Name'
    for index, row in df.iterrows():
        name = row['Names']
        print( name, ' : ', len(name) )
        output_pdf_path = os.path.join(os.path.dirname(csv_file_path), f'updated_{index + 1}.pdf')
        
        # Normalized RGB color values
        # darkslategray = (47/255, 79/255, 79/255)  #
        # steelblue = (70/255, 130/255, 180/255)  # Normalized RGB
        # teal = (0,128/255,128/255)

        # Customize font type, size, and color here
        # insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 315, font_name='Helvetica-Bold', font_size=25, font_color=( 0,0.5,0.5 ) )  # teal color
        # insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 315, font_name='Times-Bold', font_size=25, font_color=(0.184, 0.31, 0.31) )  # darkslategray color
        # insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 310, font_name='Courier-Bold', font_size=22, font_color=(0.274, 0.51, 0.706) )  # steelblue color
        # insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 310, font_name='Helvetica-Bold', font_size=20, font_color=(0.274, 0.51, 0.706) )  # steelblue color

        if len(name) >= 24:
            insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 310, font_name='Helvetica-Bold', font_size=17.5, font_color=(0.274, 0.51, 0.706) )  # steelblue color
        else:
            insert_name_into_pdf( template_pdf_path, output_pdf_path, name, 325, 310, font_name='Helvetica-Bold', font_size=20, font_color=(0.274, 0.51, 0.706) )  # steelblue color
# Example usage
csv_file_path = 'input.csv'  # Path to your CSV file
template_pdf_path = 'Cert-1.pdf'  # Path to your template PDF
process_csv_and_update_pdfs(csv_file_path, template_pdf_path)
