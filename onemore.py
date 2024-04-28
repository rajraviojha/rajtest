from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Open a URL (for example, Google's homepage)
driver.get("https://www.google.com")

# Print the title of the page
print("Title of the page:", driver.title)

# Close the browser when done
driver.quit()
