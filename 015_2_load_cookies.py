import time

from selenium import webdriver
import pickle

driver = webdriver.Chrome()
driver.get('https://www.discogs.com/')

for cookies in pickle.load(open('session', 'rb')):
    driver.add_cookie(cookies)
print('ok')
driver.refresh()
time.sleep(5)

driver.get('https://www.discogs.com/ru/sell/item/1359609013')
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/aside/div/div[1]/div/div/div/a').click()
print('ok')
time.sleep(5)
driver.quit()

