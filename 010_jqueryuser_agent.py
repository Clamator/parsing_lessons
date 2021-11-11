# есть такой метод вывода данных, как автоматизированная подгрузка данных.
# например, есть длинный список товаров, и при прокрутке вниз он подгружается дальше.
# в парсинге таких данных нам поможет jquery
# также переходим в раздел сеть, тыкаем после прокрутки на ссылку, заголовки - там видим ссылку,
# https://catertrax.com/why-catertrax/traxers/page/1/?themify_builder_infinite_scroll=yes
# так вот,там также можно просто подгружать данные и парсить их
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
# на некоторых ресурсах прокрутка может кончиться ошибкой 404, на некоторых просто пустой страницей.
# надо все это смотреть и проверять.
# в нашем случае ошибка 404 выдаваться не будет, будет возвращаться пустой контейнер без данных.

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a', newline='') as file:
        order = ['client_since', 'author', 'article_header']
        writer = csv.DictWriter(file, delimiter=',', fieldnames=order)
        writer.writerow(data)


# в данном случае мы будем искать контейнер с данными в цикле уайл и выгружать оттуда данные в список методом
# find_all, в один момент этот список будет пустым, что нам нужно отловить, проверить и закончить парсинг
def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find('div',
                         {'class': 'testimonial-container'}).find_all(
        'article')
    return articles


def get_article_data(articles):
    for article in articles:
        try:
            client_since = article.find('p', {'class': 'traxer-since'}).text.strip()
        except:
            client_since = 'empty'
        try:
            author = article.find('p', {'class': 'testimonial-author'}).text.strip()
        except:
            author = 'empty'
        try:
            article_header = article.find('h2').text.strip()
        except:
            article_header = 'empty'

        data = {
            'client_since': client_since,
            'author': author,
            'article_header': article_header
        }
        write_csv(data)


def main():
    # получить контейнер с отзывами и списка отзывов
    # если список есть - парсим отзывы
    # если список пустой - прерываем цикл

    page = 1
    while True:
        url = f'https://catertrax.com/why-catertrax/traxers/page/{str(page)}/'
        article_list = get_articles(get_html(url))  # тут или [], или [a, b, c]
        if article_list:
            get_article_data(article_list)
            page += 1
            print(url)
        else:
            print('all reviews are parsed')
            break


if __name__ == '__main__':
    main()
