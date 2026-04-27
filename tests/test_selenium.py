import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
