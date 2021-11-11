import requests
import csv
from multiprocessing import Pool

from src.deco import measure_time


def get_not_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('LI_websites.csv', 'a', encoding='utf-8', newline='') as file:
        order = ['name', 'url', 'traffic', 'percentage', 'access']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_page_data(text):  # просто получает страницу и парсит, потом записывает в файл
    data = text.strip().split('\n')[1:]  # убрали ненужные символы, вернули список строк
    # тут идет срез со второго элемента, потому что первый элемент был таким - всего\t184681\t0\t0
    for row in data:
        columns = row.strip().split('\t')[
                  :-1]  # тут я делаю срез, потому что был непонятный столбец с одной буквой s
        name = columns[0]
        url = columns[1]
        traffic = columns[3]
        percentage = columns[4]
        access = columns[-1]
        # тут построчно данные вносятся в каждый отдельный словарик
        data = {
            'name': name,
            'url': url,
            'traffic': traffic,
            'percentage': percentage,
            'access': access
        }

        write_csv(data)

# ф-я, объединяющая в себе две
def make_all(url):
    text = get_not_html(url)
    get_page_data(text)

@measure_time
def main():
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 101)]
    with Pool(10) as p:
        p.map(make_all, urls)



if __name__ == '__main__':
    main()
    # it took 1.14 to execute <function main at 0x000001BCCD1AB9D0>