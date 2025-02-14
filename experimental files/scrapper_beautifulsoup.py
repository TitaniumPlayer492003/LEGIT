import requests
from bs4 import BeautifulSoup

# URL of the specific case document
url = "https://indiankanoon.org/doc/152416473/"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <p> and <blockquote> tags within the body of the page
p_tags = soup.find_all('p')
blockquote_tags = soup.find_all('blockquote')

# Collect the text from these tags
case_text = ""

# Extract text from <p> tags
for p in p_tags:
    case_text += p.get_text(separator="\n", strip=True) + "\n"

# Extract text from <blockquote> tags
for blockquote in blockquote_tags:
    case_text += blockquote.get_text(separator="\n", strip=True) + "\n"

# Save the extracted text to a .txt file
with open('case_document.txt', 'w', encoding='utf-8') as file:
    file.write(case_text)

print("Case text saved to case_document.txt")
