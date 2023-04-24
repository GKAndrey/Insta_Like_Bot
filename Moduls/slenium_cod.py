from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

acaunt = {"redboollhih@gmail.com": '635536778', "realms101": "8889993236"}


def like(inputs: list):
    for i in acaunt.keys():
        service = Service(executable_path=os.path.abspath(__file__ + "/..") + "/chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.instagram.com')
        time.sleep(1)
        username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(i)
        password_input.send_keys(acaunt[i])
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(4)
        for j in inputs:
            driver.get(j)
            time.sleep(4)
            button_like = driver.find_element(By.CLASS_NAME, "_aamw")
            button_like.click()
            time.sleep(4)
