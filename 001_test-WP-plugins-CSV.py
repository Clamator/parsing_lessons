import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/legkovie/jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(URL, headers=HEADERS, params=params)
    return r


def parse():
    html = get_html(URL)
    if 200 <= html.status_code <= 299:
        get_content(html.text)
    else:
        raise ValueError('Error')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='unstyle characteristic')
    print(items)

if __name__ == '__main__':
    parse()
