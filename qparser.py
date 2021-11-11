from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/')
    main_page = driver.page_source
    print(main_page)

    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

if __name__ == '__main__':
    main()


t=10
while t:

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(3)


driver.execute_script("scrollBy(0,+1000);")
    sleep(3)


driver.execute_script("scrollBy(0,+1000);")
sleep(3)
t=t-1       # it a part of the loop