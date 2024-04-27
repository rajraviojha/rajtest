import pytest
from selenium import webdriver  # Add this import statement
import time

@pytest.fixture(scope="module")
def browser():
    # Specify the path to your Chromedriver binary
    driver_path = "/usr/bin/test123/chromedriver-linux64/chromedriver"

    # Set Chrome options to start the browser maximized
    options = webdriver.ChromeOptions()
    # Further configurations can be added here if needed
    options.add_argument("--start-maximized")

    # Initialize the Chrome browser with the specified options and WebDriver path
    browser = webdriver.Chrome(executable_path=driver_path, options=options)

    # Return the browser instance
    yield browser

    # Teardown - close the browser after the test completes
    browser.quit()

# Add your test methods here
  

def test_todo_app(browser):
    # Your test code here
    pass


def test_todo_app(browser):
    # Navigate to the application URL
    app_url = "http://3.87.145.157:5000/"
    browser.get(app_url)

    # Find the input field and submit button for adding a task
    input_field = browser.find_element(By.XPATH, "//*[@id='taskContent']")
    submit_button = browser.find_element(By.XPATH, "//*[@id='addTaskForm']/button")

    # Add three tasks
    for i in range(3):
        task_name = f"New task {i+1}"
        input_field.send_keys(task_name)
        submit_button.click()
        assert input_field.get_attribute("value") == ""
        print(f"Added task: {task_name}")

        # Add a small delay to ensure the task is added before adding the next one
        time.sleep(1)

    # Check if the tasks are added
    task_elements = browser.find_elements(By.CLASS_NAME, "taskContent")
    assert len(task_elements) == 3
    print("Tasks added successfully.")

    # Find all "Mark as Complete" buttons and click on them
    complete_buttons = browser.find_elements(By.CLASS_NAME, "completeButton")
    print(f"Total Mark as Complete buttons: {len(complete_buttons)}")
    for _ in range(len(complete_buttons)):
        complete_buttons[0].click()
        print("Clicked on Mark as Complete button.")

    # Verify if all tasks are marked as completed
    completed_tasks = browser.find_elements(By.CLASS_NAME, "completed")
    assert len(completed_tasks) == 3
    print("All tasks marked as completed.")

    # Find all "Delete" buttons and click on them
    delete_buttons = browser.find_elements(By.CLASS_NAME, "deleteButton")
    print(f"Total Delete buttons: {len(delete_buttons)}")
    for _ in range(len(delete_buttons)):
        delete_buttons[0].click()
        print("Clicked on Delete button.")

    # Verify if all tasks are deleted
    remaining_tasks = browser.find_elements(By.CLASS_NAME, "taskContent")
    assert len(remaining_tasks) == 0
    print("All tasks deleted.")

