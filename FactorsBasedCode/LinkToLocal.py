import requests
from bs4 import BeautifulSoup
import re
import os
from tqdm import tqdm
from colorama import Fore, Style, init
import json

# Initialize colorama for color support in terminal
init(autoreset=True)

def clean_college_name(name):
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name.lower()

# URL of the rankings page
url = "https://www.nirfindia.org/Rankings/2024/CollegeRanking.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

rows = soup.find_all('tr')

download_directory = os.path.join(os.getcwd(), "ExtractPdfData")
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

college_urls = []

for row in rows:
    try:
        college_name = row.find_all('td')[1].text.strip()
        clean_name = clean_college_name(college_name)

        pdf_link_tag = row.find('a', href=lambda href: href and '.pdf' in href)
        if pdf_link_tag:
            pdf_url = pdf_link_tag['href']

            college_urls.append({
                "college_name": clean_name,
                "url": pdf_url
            })

    except (IndexError, AttributeError):
        continue

# Displaying a nice start message
print(f"{Fore.CYAN}Starting the download of PDF files...{Style.RESET_ALL}")
print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}\n")

# Download each PDF with a progress bar and animation
for college in tqdm(college_urls, desc=f"{Fore.GREEN}Downloading PDFs{Style.RESET_ALL}", ncols=100, bar_format="{l_bar}{bar}{r_bar}", colour="green"):
    file_name = f"{college['college_name']}.pdf"
    file_path = os.path.join(download_directory, file_name)

    pdf_response = requests.get(college['url'])
    
    with open(file_path, 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

# Completion message with animation
print(f"\n{Fore.GREEN}{'=' * 50}")
print(f"{Fore.MAGENTA}All PDFs downloaded successfully!{Style.RESET_ALL}\n")

# Save the data to JSON
output_json_path = "college_urls.json"
with open(output_json_path, 'w') as json_file:
    json.dump(college_urls, json_file, indent=4)

# Print final message in color
print(f"{Fore.MAGENTA}College URLs extracted and saved to {output_json_path}{Style.RESET_ALL}")
