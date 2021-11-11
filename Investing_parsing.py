import requests
from bs4 import BeautifulSoup


def get_html(url, params=None):
    text = requests.get(url, headers=HEADERS, params=params)
    return text.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    print(trs)
    for tr in trs:
       tds = tr.find_all('td')
       name = tds[1].find('a').text
       print(tds)


def main():
    url = 'https://ru.investing.com/crypto/currencies'
    print(get_html(url))


if __name__ == '__main__':
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'accept': '*/*'}
    main()
