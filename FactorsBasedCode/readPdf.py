import pdfplumber
import pandas as pd
import json
import re

def clean_column_name(column_name):
    """
    Cleans the column name by:
    1. Removing special characters.
    2. Replacing spaces with underscores for snake_case.
    3. Removing newline characters.
    """
    # Remove special characters except for spaces and underscores
    column_name = re.sub(r'[^a-zA-Z0-9\s]', '', column_name)
    # Replace spaces and newlines with underscores
    column_name = re.sub(r'\s+', '_', column_name.strip())
    return column_name.lower()

# Specify the path to the PDF file
pdf_path = r"C:\Users\Admin\Documents\Work\XtraCut_Works\Publisher-Portal-scrapping-v1\FactorsBasedCode\ExtractPdfData\IR-C-C-6377.pdf"  # Update this path if the PDF is in another location


# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    all_tables = []
    
    # Loop through all pages
    for page_num, page in enumerate(pdf.pages):
        # Extract tables from the page
        tables = page.extract_table()
        
        if tables:
            # Clean the column headers
            clean_headers = [clean_column_name(header) for header in tables[0]]
            
            # Convert the table into a pandas DataFrame using the cleaned headers
            df = pd.DataFrame(tables[1:], columns=clean_headers)
            
            # Convert DataFrame to a dictionary
            table_data = df.to_dict(orient="records")
            
            # Append the table data to the list of all tables
            all_tables.append({
                "page": page_num + 1,
                "table": table_data
            })

# Convert the list of tables into JSON
json_data = json.dumps(all_tables, indent=4)

# Save the JSON data to a file
output_json_path = "extracted_tables_cleaned.json"
with open(output_json_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Table data extracted, cleaned, and saved to {output_json_path}")
