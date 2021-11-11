from datetime import datetime, date, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time


def write_csv(data):
    with open('ears.csv', 'a', encoding='utf-8', newline='') as file:
        order = ['name', 'price_min', 'price_max', 'date']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_ears():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.headless = True
    ears = 'https://www.e-katalog.ru/k239.htm'
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(ears)

    sony_button = driver.find_element_by_xpath("//a[contains(text(), 'Sony')]")
    driver.execute_script('arguments[0].click();', sony_button)

    min_price = driver.find_element_by_id('minPrice_')
    min_price.send_keys(int(3000))

    max_price = driver.find_element_by_id('maxPrice_')
    max_price.send_keys(int(15000))

    #mini_jack_true = driver.find_element_by_xpath(
    #    '/html/body/div[5]/table/tbody/tr/td[2]/div/div[1]/div[2]/form/div[5]/ul[4]/li[1]/label')
    #driver.execute_script("arguments[0].click();", mini_jack_true)

    view_all = driver.find_element_by_class_name('submit-button')
    driver.execute_script("arguments[0].click();", view_all)

    main_table = driver.find_elements_by_css_selector('div[class*="model-short-div list-item--goods   "]')
    # table = driver.find_element_by_class_name('main-part-content')
    for el in main_table:
        a_e = el.find_elements_by_css_selector('table[class*="model-short-block"]')
        for el in a_e:
            name = el.find_element_by_css_selector('span.u').text

            try:
                price_min = el.find_element_by_css_selector('div.model-price-range').find_elements_by_tag_name('span')[
                    0].text
            except:
                price_min = 'no data'  # el.find_element_by_css_selector('div.pr31').text

            try:
                price_max = el.find_element_by_css_selector('div.model-price-range').find_elements_by_tag_name('span')[
                    1].text
            except:
                price_max = 'no data'  # el.find_element_by_css_selector('div.pr31').text

            data = {
                'name': name,
                'price_min': price_min,
                'price_max': price_max,
                'date': datetime.now()
            }

            print(data)
            write_csv(data)


if __name__ == '__main__':
    get_ears()
