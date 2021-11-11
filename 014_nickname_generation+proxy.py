from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

option.headless = True
#option.add_argument('--proxy-server=37.112.34.55:8080')

driver = webdriver.Chrome(chrome_options=option)
driver.get("https://mynickname.com/generate")

for x in range(4):
    xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    driver.find_element_by_xpath(xpath).click()
    name = driver.find_element_by_id("register").get_attribute('href')[37:]
    print(name)

driver.quit()

# бесплатные прокси серверы походу работают криво и нестабильно