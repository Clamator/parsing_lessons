import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    resp = requests.get(url)
    return resp.text


def refined(s):
    # принимает строку в таком виде: (1,016 total ratings)
    r = s.split(' ')[0]
    result = r.replace(',', '')
    return result
    # возвращает строку в таком виде: 1016


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)  # создали переменную, которая применяет ф-ю к каждой строке
        # но для этого нам надо создать или список,или кортеж из файла data
        writer.writerow((data['name'],
                         data['url'],
                         data['rating'],
                         data['review_link'],
                         data['description']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured_section = soup.find_all('section')[1]  # здесь мы берем только конкретный раздел из 4-х, СПИСОК
    # x = featured_section.find('h2').text - вывод названия раздела плагинов
    featured_plugins = featured_section.find_all('article')  # здесь СПИСОК плагинов из конкретного раздела

    for plugin in featured_plugins:  # <class 'bs4.element.Tag'> - тип данных "плагина"
        name = plugin.find('h3').text  # имена находятся в этом теге, вывод именно имен, ибо text
        url = plugin.find('h3').find('a').get('href')  # тут берет список плагинов, ищет вложенный тег "а", и по
        # нему ищет атрибут тега через метог ГЕТ.
        # rating = plugin.find('div', class_='plugin-rating').text  # выводит str: (1,016 total ratings)
        reviews = plugin.find('span', class_='rating-count').find('a').get('href')  # ссылки на обзоры плагинов
        rate = plugin.find('span', class_='rating-count').find('a').text  # выводит str: 1,016 total ratings
        # как видим, есть еще приписка "total ratings", а у цифр есть запятые. При записи в CSV файл нужно будет
        # нормализацию, это чтобы все данные были как надо, убрать лишнее, будем делать в отдельной ф-и

        rating = refined(rate)
        description = plugin.find('div', class_='entry-excerpt').find('p').text


        # для записи данных в CSV-файл, их нужно записать в словарь
        data = {
            'name': name,
            'url': url,
            'rating': rating,
            'review_link': reviews,
            'description': description
        }
        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
# 37 минут