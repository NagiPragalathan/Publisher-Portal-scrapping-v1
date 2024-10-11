import requests
from bs4 import BeautifulSoup
import re, os

# Function to clean and convert college names to snake_case
def clean_college_name(name):
    # Remove special characters except for spaces and underscores
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    # Replace spaces and newlines with underscores
    name = re.sub(r'\s+', '_', name.strip())
    return name.lower()

# URL of the rankings page
url = "https://www.nirfindia.org/Rankings/2024/CollegeRanking.html"

# Send a GET request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all table rows with college details
rows = soup.find_all('tr')

# Initialize a list to store the results
college_urls = []

# Loop through each row and extract college names and URLs
for row in rows:
    try:
        # Extract the college name (second <td> element in each row)
        college_name = row.find_all('td')[1].text.strip()
        # Clean the college name to snake_case
        clean_name = clean_college_name(college_name)

        # Extract the PDF link using <a> tags that contain '.pdf'
        pdf_link_tag = row.find('a', href=lambda href: href and '.pdf' in href)
        if pdf_link_tag:
            pdf_url = pdf_link_tag['href']

            # Store the cleaned name and corresponding URL in a dictionary
            college_urls.append({
                "college_name": clean_name,
                "url": pdf_url
            })

    except (IndexError, AttributeError):
        # Handle cases where rows do not match expected structure
        continue

# Print the extracted college names and URLs
for college in college_urls:
    print(college)

# Optionally, you can save this data as JSON
import json

current_path = os.path.dirname(os.path.abspath(__file__))

save_path = os.path.join(current_path,"ExtractPdfData", "college_urls.json")


with open(save_path, 'w') as json_file:
    json.dump(college_urls, json_file, indent=4)

print(f"College URLs extracted and saved to {save_path}")
