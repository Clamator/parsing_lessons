import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(url)
    return resp.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    #main_sec = soup.find('section', class_='top_news').find('h2').text
    main_news = soup.find_all('article', class_='top_news__item')


    for news in main_news:
        name = news.find('h2').text
        read_news = news.find('a').get('href')
        print(f'{name}, https://www.kommersant.ru/{read_news}')


def main():
    url = 'https://www.kommersant.ru/'
    get_data(get_html(url))

if __name__ == '__main__':
    main()