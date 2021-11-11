from fake_user_agent.main import user_agent
import requests
from bs4 import BeautifulSoup
import csv


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='table_block mpitems push_down table_responsive').find('tbody').find_all('tr')

    links = []
    for tr in trs:
        tds = tr.find_all('td')
        try:
            artist = tds[1].find('a').text.strip()
        except:
            artist = 'no name'
        #print(artist)

        try:
            shipper = tds[2].find_all('li')[2].text[16:]
        except:
            shipper = 'no shipper'
        #print(shipper)

        #if 'Russian Federation' in shipper:
        #    shipper = shipper
        #else:
        #    shipper = None
        #print(shipper)

        try:
            add_to_cart = 'https://www.discogs.com'+tds[-1].find('a').get('href')

        except:
            add_to_cart = 'no button'

        if 'discogs.com' in add_to_cart:
            links.append(add_to_cart)


    for el in links:
        requests.get(el)

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

    discs_list = 'https://www.discogs.com/ru/sell/list?master_id=229651&ev=mb'
    profile_response = session.get(discs_list).text.strip()
    get_page_data(profile_response)


if __name__ == '__main__':
    main()
