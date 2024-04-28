from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # To run Chrome in headless mode (without GUI)

# Path to the Chrome WebDriver executable (ensure it's in your PATH or specify the full path)
chrome_driver_path = "/usr/local/bin/webdriver"

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Open google.com
driver.get("https://www.google.com")

# Print the title of the page
print("Title of the page:", driver.title)

# Close the browser
driver.quit()
