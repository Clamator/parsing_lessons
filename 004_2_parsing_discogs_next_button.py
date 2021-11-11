
import requests

from bs4 import BeautifulSoup
import csv


def get_html(url):
    resp = requests.get(url)
    return resp.text


def write_csv(data):
    with open('discogs2.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['fullname'],
            data['label'],
            data['buy_link'],
            data['release_link']
        ))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='table_block mpitems push_down table_responsive').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            fullname = tds[1].find('strong').text.strip()
        except:
            fullname = ''

        try:
            label = tds[1].find('p', class_='hide_mobile label_and_cat').find('a').text.strip()
        except:
            label = ''

        try:
            link = 'https://www.discogs.com' + tds[1].find('strong').find('a').get('href')
        except:
            link = ''

        try:
            release_link = 'https://www.discogs.com' + tds[1].find('p', class_='hide_mobile').find('a').get('href')
        except:
            release_link = ''

        data = {
            'fullname': fullname,
            'label': label,
            'buy_link': link,
            'release_link': release_link
        }
        write_csv(data)

        print(f'artist/album: {fullname}, LABEL: {label}, {link}')


def main():
    url = 'https://www.discogs.com/ru/sell/list?style=Pop+Rock&page=1'
    x = 0
    while x <=3:
        get_page_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')
        try:
            url = 'https://www.discogs.com/'+soup.find('ul', class_='pagination_page_links').find('a', class_='pagination_next').get('href')
        except:
            print('All pages are parsed')
            break

        x+=1


if __name__ == '__main__':
    main()


