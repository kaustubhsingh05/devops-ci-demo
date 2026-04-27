import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

URL = 'http://localhost:8000'

@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_show_message(driver):
    driver.get(URL)
    button = driver.find_element(By.ID, 'show-message-btn')
    button.click()
    message = driver.find_element(By.ID, 'message').text
    assert message == 'Hello from the DevOps CI Demo web app!'

def test_increment_counter(driver):
    driver.get(URL)
    increment_btn = driver.find_element(By.ID, 'increment-btn')
    counter = driver.find_element(By.ID, 'counter')
    initial_text = counter.text
    assert 'Counter: 0' in initial_text
    increment_btn.click()
    updated_text = counter.text
    assert 'Counter: 1' in updated_text

def test_display_text(driver):
    driver.get(URL)
    text_input = driver.find_element(By.ID, 'text-input')
    display_btn = driver.find_element(By.ID, 'display-text-btn')
    displayed_text = driver.find_element(By.ID, 'displayed-text')
    text_input.send_keys('Test input')
    display_btn.click()
    assert 'You entered: Test input' in displayed_text.text

def test_toggle_dark_mode(driver):
    driver.get(URL)
    toggle_btn = driver.find_element(By.ID, 'toggle-theme-btn')
    body = driver.find_element(By.TAG_NAME, 'body')
    initial_class = body.get_attribute('class')
    assert 'dark' not in initial_class
    toggle_btn.click()
    updated_class = body.get_attribute('class')
    assert 'dark' in updated_class

def test_calculator_addition(driver):
    driver.get(URL)
    num1_input = driver.find_element(By.ID, 'num1')
    num2_input = driver.find_element(By.ID, 'num2')
    add_btn = driver.find_element(By.ID, 'add-btn')
    result_div = driver.find_element(By.ID, 'result')
    num1_input.send_keys('5')
    num2_input.send_keys('3')
    add_btn.click()
    assert 'Result: 8' in result_div.text

def test_add_todo(driver):
    driver.get(URL)
    todo_input = driver.find_element(By.ID, 'todo-input')
    add_todo_btn = driver.find_element(By.ID, 'add-todo-btn')
    todo_list = driver.find_element(By.ID, 'todo-list')
    todo_input.send_keys('Test todo')
    add_todo_btn.click()
    todos = todo_list.find_elements(By.TAG_NAME, 'li')
    assert len(todos) == 1
    assert 'Test todo' in todos[0].text

def test_random_color_generator(driver):
    driver.get(URL)
    random_color_btn = driver.find_element(By.ID, 'random-color-btn')
    color_display = driver.find_element(By.ID, 'color-display')
    random_color_btn.click()
    text = color_display.text
    assert 'Generated color:' in text
    # Check if it contains a hex color
    import re
    hex_match = re.search(r'#[0-9a-fA-F]{6}', text)
    assert hex_match is not None
    toggle_btn.click()
    updated_class = body.get_attribute('class')
    assert 'dark' in updated_class
