from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/autocomplete')

chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Pri')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('saca')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter address"]').send_keys(' Dornei')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="City"]').send_keys('Bucuresti')
sleep(2)

chrome.quit()