# есть такая тема, когда у страницы не привычный HTML код, а совсем другая методика работы
# ее суть заключается в том, что у каждой страницы нет своего конкретного кода для какого-то контента в виде HTML,
# а при переходе на другую страницу с контентом перезагружается не вся страница, а только ее часть. Например, у нас
# есть огромный список сайтов, на каждой странице их 30 штук, если мы просто будем использовать пагинацию и обычную
# замену номера страницы в ссылке, то у нас ничего не получится. Работает примерно так: при нажатии кнопки для перехода
# на другую страницу обновляется не вся страница, а на сервер отправляется запрос, сервер его обрабатывает и выдает
# просто набор данных, которые подставляются на место предыдущей инфы. Если открыть код страницы, то в разделе сеть/xhr
# мы смодем увидеть ссылку страницы, который будет отличен от той, которую мы видем в адресной строке.
# и меняя номер страницы по этой ссылке уже можно будет увидеть обновление данных
# т.к. реквест не умеет работать с джаваскрипт, мы будем парсить ответ сервера
# поэтому нам надо отпределить адрес, куда мы будем слать запрос, метод и параметры, если они нужны

import requests
import csv

from src.deco import measure_time


def get_not_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('LI_websites.csv', 'a', encoding='utf-8', newline='') as file:
        order = ['name', 'url', 'description', 'traffic', 'percentage', 'access']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


@measure_time
def main():
    for i in range(1, 101):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={str(i)}'
        server_response = get_not_html(url)
        data = server_response.strip().split('\n')[1:]  # убрали ненужные символы, вернули список строк
        # тут идет срез со второго элемента, потому что первый элемент был таким - всего\t184681\t0\t0
        for row in data:
            columns = row.strip().split('\t')[
                      :-1]  # тут я делаю срез, потому что был непонятный столбец с одной буквой s
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percentage = columns[4]
            access = columns[-1]
            # тут построчно данные вносятся в каждый отдельный словарик
            data = {
                'name': name,
                'url': url,
                'description': description,
                'traffic': traffic,
                'percentage': percentage,
                'access': access
            }

            write_csv(data)


if __name__ == '__main__':
    main()
    # it took 14.88 to execute <function main at 0x0000026DA62CB550>