from time import sleep
from selenium import webdriver

option = webdriver.FirefoxOptions()
#option.add_argument("--disable-blink-features=AutomationControlled")
option.set_preference('dom.webdriver.enable', False)

driver = webdriver.Firefox()
driver.get("https://mynickname.com/generate")

for x in range(4):
    xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    driver.find_element_by_xpath(xpath).click()
    name = driver.find_element_by_id("register").get_attribute('href')[37:]
    print(name)