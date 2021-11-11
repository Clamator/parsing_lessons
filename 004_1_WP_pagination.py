#  делаем пагинацию на плагинах wordpress
import requests
from bs4 import BeautifulSoup
import csv

from src.deco import measure_time


def get_html(url):
    resp = requests.get(url)
    if resp.ok:
        return resp.text
    print(resp.status_code)


def write_csv(data):
    with open('plugins2.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['rating'],
                         data['author'],
                         data['link']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured_plugins = soup.find_all('article')

    for plugin in featured_plugins:
        try:
            name = plugin.find('h3').text.strip()
        except:
            name = ''

        try:
            rating = plugin.find('span', class_='rating-count').text.strip()
        except:
            rating = ''

        try:
            author = plugin.find('span', class_='plugin-author').text.strip()
        except:
            author = ''
        try:
            link = plugin.find('h3').find('a').get('href')
        except:
            link = ''

        data = {
            'name': name,
            'rating': rating,
            'author': author,
            'link': link
        }

        write_csv(data)

@measure_time
def main():
    pattern = 'https://wordpress.org/plugins/browse/blocks/page/{}/'
    for x in range(1, 25):
        url = pattern.format(str(x))
        get_data(get_html(url))


if __name__ == '__main__':
    main()
# it took 17.70 to execute <function main at 0x000001C898F56940>