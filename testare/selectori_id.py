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

contact_link = chrome.find_element(By.ID, 'contact-link')
sleep(2)
contact_link.click()
sleep(2)

email = chrome.find_element(By.ID, 'email')
sleep(2)
email.send_keys('monica@gmail.com')
sleep(2)

id_order = chrome.find_element(By.ID, 'id_order')
sleep(2)
id_order.send_keys('alabalaportocala')
sleep(2)

message = chrome.find_element(By.ID, 'message')
sleep(2)
message.send_keys('buna ziua')
sleep(2)

submit = chrome.find_element(By.ID, 'submitMessage')
sleep(2)
submit.click()
sleep(2)

chrome.quit()
