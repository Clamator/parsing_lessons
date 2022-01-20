from fake_user_agent.main import user_agent
import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open('discogs3.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['artist'],
            data['artist_link'],
            data['release_name'],
            data['release_link'],
            data['label'],
            data['label_link'],
            data['in_stock'],
            data['format'],
            data['release_year']
        ))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='release_list_table table_block table_responsive cw_public layout_med').find(
        'tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            artist = tds[2].find('a').text.strip()
        except:
            artist = 'no name'

        try:
            artist_link = tds[2].find('a').get('href')
        except:
            artist_link = 'no link'

        try:
            release_name = tds[2].find_all('a')[1].text.strip()
        except:
            release_name = 'no link'

        try:
            release_link = tds[2].find_all('a')[1].get('href')
        except:
            release_link = 'no link'

        try:
            label = tds[2].find_all('span')[0].find_all('a')[
                2].text.strip()  # tds[2].find_all('span')[0].find('br').get_text(), tds[2].find_all('span')[0].get_text()
        except:
            label = 'no link'

        try:
            label_link = tds[2].find_all('span')[0].find_all('a')[2].get('href')
        except:
            label_link = 'no link'

        try:
            in_stock = tds[2].find_all('span')[1].text.strip()
        except:
            in_stock = 'no link'

        try:
            format = tds[3].text.strip()
        except:
            format = 'no link'

        try:
            release_year = tds[4].text.strip()
        except:
            release_year = 'no link'

        try:
            no = tds[-1]
        except:
            no = 'no link'

        data = {
            'artist': artist,
            'artist_link': 'https://www.discogs.com' + artist_link,
            'release_name': release_name,
            'release_link': 'https://www.discogs.com' + release_link,
            'label': label,
            'label_link': label_link,
            'in_stock': in_stock,
            'format': format,
            'release_year': release_year
        }
        write_csv(data)


def main():
    link = 'https://accounts.discogs.com/login'
    user = user_agent("firefox")

    session = requests.Session()

    header = {
        'user-agent': user
    }

    data = {
        'username': 'Clamator',
        'password': 'Munroe23'
    }

    response = session.post(link, data=data, headers=header).text

    profile_link = 'https://www.discogs.com/ru/user/Clamator/collection?page=1'
    profile_response = session.get(profile_link).text.strip()
    get_page_data(profile_response)


if __name__ == '__main__':
    main()
