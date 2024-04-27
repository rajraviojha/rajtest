import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set the path to ChromeDriver executable
chrome_driver_path = "/usr/bin/test123/chromedriver-linux64/chromedriver"

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set Chrome service
chrome_service = Service(chrome_driver_path)

# Initialize Chrome WebDriver with service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


@pytest.fixture(scope="module")
def browser():
    # Set Chrome options to start the browser maximized
    options = webdriver.ChromeOptions()
    # Further configurations can be added here if needed
    options.add_argument("--start-maximized")

    # Initialize the Chrome browser with the specified options
    browser = webdriver.Chrome(options=options)

    # Return the browser instance
    yield browser

    # Teardown - close the browser after the test completes
    browser.quit()


def test_todo_app(browser):
    # Your test code here
    pass

# Add your test methods here
