# import pandas as pd

# df = pd.read_csv('input.csv')
# nameList = df['Names'].values.tolist()
# # print( nameList, end=',' )

# for i in range( len(nameList) ):
#     ppName = nameList[i]
#     print( ppName, end=',' )

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def insert_string_into_pdf(original_pdf_path, new_pdf_path, text_to_insert, x, y, page_number=0):
    # Read the original PDF
    reader = PdfReader(original_pdf_path)
    writer = PdfWriter()
    
    # Create a PDF to overlay with the new string
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Insert the string on the specified page
    can.drawString(x, y, text_to_insert)
    can.showPage()
    
    can.save()
    
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    overlay_pdf = PdfReader(packet)
    
    # Merge the original PDF with the new overlay PDF
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        if i == page_number:  # Insert on the specified page
            overlay_page = overlay_pdf.pages[0]
            page.merge_page(overlay_page)
        writer.add_page(page)
    
    # Write the updated PDF to a file
    with open(new_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

# Example usage
insert_string_into_pdf('Cert-1.pdf', 'updated_template.pdf', 'Rohan!', 100, 100, page_number=0)