import time

import wget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_links():
    option = Options()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.headless = True
    driver = webdriver.Chrome(chrome_options=option)
    start_page = 'https://vk.com/album-114966187_2750426972'
    driver.get(start_page)
    for _ in range(5):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            continue
        time.sleep(0.1)
    pics = driver.find_elements(By.CLASS_NAME, 'photos_row ')

    all_links = []
    for pic in pics:
        link = pic.find_element(By.CSS_SELECTOR, 'a[data-photo-id*="-114966187"]').get_attribute('href')
        all_links.append(link)

    new_links = []
    for new_link in all_links:
        driver.get(new_link)
        time.sleep(0.2)
        try:
            photo_link = driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            print(photo_link)
        except:
            photo_link = 'none'
            print(photo_link)
        new_links.append(photo_link)
    return  new_links

def wget_download(urls):
    directory = 'F:\Test2'
    for url in urls:
        wget.download(url, out=directory)


if __name__ == '__main__':
    wget_download(get_links())
