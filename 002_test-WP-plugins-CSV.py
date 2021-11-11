import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(url)
    return resp.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    featured_plugins = soup.find_all('article')

    for plugin in featured_plugins:
        name = plugin.find('h3').text
        rating = plugin.find('span', class_='rating-count').text
        descr = plugin.find('div', class_='entry-excerpt').text
        author = plugin.find('span', class_='plugin-author').text
        print(name)

def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
