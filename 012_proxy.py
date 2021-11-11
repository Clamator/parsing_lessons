import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')
    table_rows = soup.find('table').find_all('tr')[1:50]

    proxies = []

    for table_row in table_rows:
        table_data = table_row.find_all('td')
        ip = table_data[0].text.strip()
        port = table_data[1].text.strip()
        schema = 'https' if 'yes' in table_data[6].get_text(strip=True) else 'http'

        proxy = {
            'schema': schema,
            'address': ip + ':' + port
        }
        proxies.append(proxy)

    return choice(proxies)


def get_html(url):
    # для того, чтобы метод гет юзал прокси, их ему надо передать в виде аргумента
    pr = get_proxy() # тут получаем что-то в виде {'schema': 'http', 'address': '158.58.133.106:41258'}
    prox = {pr['schema']: pr['address']}
    r = requests.get(url, proxies=prox, timeout=5) # proxies=prox, но сайт в примере не https, поэтому если предлагается
    # прокся https, то выдает ошибку, т.к. незащищен
    return r.json()['origin']


def main():
    url = 'http://httpbin.org/ip'
    print(get_html(url))


if __name__ == '__main__':
    main()
# 15:26

  # "origin": "109.252.187.76"

# одним словом, используем прокси, если нас куда-то не пускает и тд