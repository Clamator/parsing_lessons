from selenium import webdriver
import pickle
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.discogs.com/')
# saving cookies
sleep(30)
pickle.dump(driver.get_cookies(), open('session_discogs', 'wb'))
driver.quit()


