import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

from selenium.webdriver.common.keys import Keys


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    x = 0
    while x <= 10:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        last_height = new_height
        x += 1

    time.sleep(1)

    main_page = driver.find_element_by_tag_name("html")
    return main_page.get_attribute("innerHTML")


def refined(s):
    # принимает строку в таком виде: (1,016 total ratings)
    result = s.replace('$', '')
    result2 = result.replace(',', '')
    return result2


def write_csv(data):
    with open('cmc5.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']])


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # trs = tr в мн.ч. - table row - просто строка таблицы
    trs = soup.find('table').find('tbody').find_all('tr')  # здесь идет вся инфа по всем валютам на странице
    # это все объекты супа, с которыми мы работаем
    for tr in trs:  # тут берем конкретную крипту, это просто строка с данными, которые еще надо достать,
        tds = tr.find_all('td')  # получаем здесь список объектов
        name = tds[2].find('a').find('p', class_='sc-1eb5slv-0 iworPT').text
        symbol = tds[2].find('a').find('p', class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        url = 'https://coinmarketcap.com/' + tds[2].find('a').get('href')
        price0 = tds[3].find('a').text
        price = refined(price0)
        print(name, symbol, url, price)

        data = {
            'name': name,
            'symbol': symbol,
            'url': url,
            'price': price
        }

        write_csv(data)


def main():
    URL = 'https://coinmarketcap.com/'
    html = get_html(URL)
    time.sleep(5)
    get_page_data(html)


if __name__ == '__main__':
    main()
