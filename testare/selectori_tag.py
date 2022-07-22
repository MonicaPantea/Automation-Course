from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('http://automationpractice.com/index.php')
sleep(2)

#
chrome.find_element(By.LINK_TEXT, 'Sign in').click()
user = chrome.find_elements(By.TAG_NAME, 'input')
sleep(2)
user[7].send_keys('Monica@gmail.com')
sleep(2)

#
parola = chrome.find_elements(By.TAG_NAME, 'input')
sleep(2)
parola[8].send_keys('iulie2022')
sleep(2)

#
submit = chrome.find_elements(By.TAG_NAME, 'button')
sleep(2)
submit[2].click()

sleep(2)
chrome.quit()
