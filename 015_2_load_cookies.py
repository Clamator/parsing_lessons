import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

driver = webdriver.Chrome()
driver.get('https://www.discogs.com/')

for cookies in pickle.load(open('session_discogs', 'rb')):
    driver.add_cookie(cookies)
print('ok')
driver.refresh()
time.sleep(5)

driver.get('https://www.discogs.com/ru/sell/item/1359609013')
load = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/aside/div/div[1]/div/div/div/a')
driver.execute_script("arguments[0].click();", load)
print('ok')
time.sleep(5)
driver.quit()

