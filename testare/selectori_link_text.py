from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')

#
link_text = chrome.find_element(By.LINK_TEXT, 'Autocomplete')

sleep(2)
link_text.click()
sleep(2)

back = chrome.find_element(By.ID, 'logo')
sleep(2)
back.click()
sleep(2)

#
link_text_2 = chrome.find_element(By.LINK_TEXT, 'Buttons')

sleep(2)
link_text_2.click()
sleep(2)

back = chrome.find_element(By.ID, 'logo')
sleep(2)
back.click()
sleep(2)

#
link_text_3 = chrome.find_element(By.LINK_TEXT, 'Key and Mouse Press')

sleep(2)
link_text_3.click()
sleep(2)

chrome.quit()