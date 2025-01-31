from selenium import webdriver

# Start Chrome WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print("Page title:", driver.title)

# Close the browser
driver.quit()
