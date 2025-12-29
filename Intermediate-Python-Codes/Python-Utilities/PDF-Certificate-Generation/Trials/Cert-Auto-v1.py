import csv
from fpdf import FPDF

# Function to read names from CSV file
def read_names_from_csv(csv_file):
    names = []
    with open(csv_file, mode='r', encoding='ISO-8859-1') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            names.append(row)
    return names

# Function to create a PDF with a given name at a specific position
def create_pdf(template_pdf, output_pdf, name, x, y):
    pdf = FPDF()
    pdf.add_page()
    
    # Add the template PDF as background
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.image(template_pdf, x=0, y=0, w=210, h=297)  # Adjust width and height as needed

    # Set font and add the name at the specified position
    pdf.set_font("Arial", size=12)
    pdf.set_xy(x, y)
    pdf.cell(0, 10, name)

    # Save the new PDF
    pdf.output(output_pdf)

# Main function to generate PDFs based on CSV input
def generate_pdfs(csv_file, template_pdf, x, y):
    names = read_names_from_csv(csv_file)
    for name in names:
        output_pdf = f"{name}.pdf"
        create_pdf(template_pdf, output_pdf, name, x, y)

# Example usage
csv_file = 'Names.csv'  # Replace with your CSV file path
template_pdf = 'Cert-1.pdf'  # Replace with your template PDF file path
x_position = 100  # Replace with your desired x position
y_position = 150  # Replace with your desired y position
generate_pdfs(csv_file, template_pdf, x_position, y_position)
