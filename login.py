import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.by import By


def driver():
    options = Options()
    headless = os.environ['SELENIUM_HEADLESS'].upper()
    if headless != 'FALSE':
        options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")  # open Browser in maximized mode
    options.add_argument("--disable-infobars")  # disabling infobars
    options.add_argument("--disable-extensions")  # disabling extensions
    options.add_argument("--disable-gpu")  # applicable to windows os only
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--ignore-certificate-errors")
    return_value = webdriver.Chrome(options=options)
    return return_value


def main():
    local_driver = driver()
    local_driver.get('https://stackoverflow.com')
    wait = WebDriverWait(local_driver, int(10))
    log_in_button = wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]'))
    )
    log_in_button.click()
    email = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'email')))
    email.send_keys(os.environ['STACKOVERFLOW_EMAIL'])
    password = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'password')))
    password.send_keys(os.environ['STACKOVERFLOW_PASSWORD'])
    submit_button = wait.until(expected_conditions.visibility_of_element_located((By.ID, 'submit-button')))
    submit_button.click()
    avatar = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/header/div/ol[2]/li[2]/a/div[1]/img')))
    avatar.click()
    user_name = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="mainbar-full"]/div[1]/div[1]/div/div[1]/div[1]')))
    print('User name:', user_name.text)
    time.sleep(1)


main()
