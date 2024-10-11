import pdfplumber
import json

# Path to the uploaded PDF
pdf_path = "C:/Users/Praveena/Desktop/Publisher-Portal-scrapping-v1/NIRF/IR-C-C-6377.pdf"

# Function to extract the PDF content
def extract_pdf_content(pdf_path):
    content = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text from each page
            text = page.extract_text()
            content.append({
                "page_number": page.page_number,
                "text": text
            })

            # Extract tables from each page
            tables = page.extract_tables()
            if tables:
                content[-1]["tables"] = tables

    return content

# Extract content from the PDF
pdf_content = extract_pdf_content(pdf_path)

# Create a file and write the extracted content
output_file_path = "C:/Users/Praveena/Desktop/Publisher-Portal-scrapping-v1/NIRF/pdf_output.json"
with open(output_file_path, 'w') as output_file:
    json.dump(pdf_content, output_file, indent=2)

print(f"Extracted content has been saved to {output_file_path}")
