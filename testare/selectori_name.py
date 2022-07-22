from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)


chrome.maximize_window()


chrome.get('http://automationpractice.com/index.php')

#
search_item = chrome.find_element(By.NAME, 'search_query')
sleep(2)
search_item.send_keys('blouse')
sleep(2)

#
clik_button_search = chrome.find_element(By.NAME, 'submit_search')
sleep(2)
clik_button_search.click()
sleep(2)

#
newsletter = chrome.find_element(By.NAME, 'email')
sleep(2)
newsletter.send_keys('anabanana@gmail')
sleep(3)


chrome.quit()