from multiprocessing import Pool

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
    start_page = 'https://nsfwalbum.com/photo/73664788'
    driver.get(start_page)

    all_links = []
    for _ in range(90):
        time.sleep(0.6)
        link = driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        all_links.append(link[:-6])
        print(link)
        time.sleep(0.2)
        next = driver.find_element(By.CSS_SELECTOR, 'a[id*="nextPhoto"]')
        driver.execute_script("arguments[0].click();", next)

    return all_links



def wget_download(urls):
    directory = 'F:\Test2'
    for url in urls:
        wget.download(url, out=directory)


if __name__ == '__main__':
    wget_download(get_links())
