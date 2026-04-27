from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'http://localhost:8000'

def run_test():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        button = driver.find_element(By.ID, 'show-message-btn')
        button.click()

        message = driver.find_element(By.ID, 'message').text
        assert 'Hello from the DevOps CI Demo web app!' in message

        print('Selenium test passed: message displayed correctly.')
    finally:
        driver.quit()

if __name__ == '__main__':
    run_test()
