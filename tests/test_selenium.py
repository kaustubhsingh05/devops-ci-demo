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
