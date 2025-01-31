from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set the path to your ChromeDriver
chrome_driver_path = '/home/titaniumplayer492003/Downloads/chromedriver-linux64/chromedriver'

# Set up Chrome options (optional, for headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Specify the Brave browser binary path
chrome_options.binary_location = "/usr/bin/brave"  # Replace with the actual path if different

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# URL of the specific case document
url = "https://indiankanoon.org/doc/152416473/"

# Open the webpage
driver.get(url)

# Extract text from the case
# Example: Extracting paragraphs and blockquotes
p_tags = driver.find_elements_by_tag_name('p')
blockquote_tags = driver.find_elements_by_tag_name('blockquote')

case_text = ""

for p in p_tags:
    case_text += p.text + "\n"

for blockquote in blockquote_tags:
    case_text += blockquote.text + "\n"

# Save the extracted text to a .txt file
with open('case_document_selenium.txt', 'w', encoding='utf-8') as file:
    file.write(case_text)

# Close the WebDriver
driver.quit()

print("Case text saved to case_document_selenium.txt")
