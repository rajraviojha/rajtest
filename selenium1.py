import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

@pytest.fixture(scope="module")
def browser():
    # Initialize the Chrome browser with the specified options
    browser = webdriver.Chrome(options=chrome_options)

    # Return the browser instance
    yield browser

    # Teardown - close the browser after the test completes
    browser.quit()

# Add your test methods here
