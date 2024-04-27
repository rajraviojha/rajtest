from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options (headless mode to run without GUI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Open google.com
driver.get("https://www.google.com")

# Verify if the title contains "Google"
if "Google" in driver.title:
    print("Google.com opened successfully!")
else:
    print("Failed to open Google.com")

# Close the browser
driver.quit()

