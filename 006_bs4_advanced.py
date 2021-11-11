from bs4 import BeautifulSoup
import re  # - регуляр выраж-я,шаблоны, по кот осущ-ся поиск


# tag - это объект супа, то есть один из сотрудников
def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    else:
        return None


def get_salary(s):  # допустим, n чел заполняют графу ЗП по разному, а нам нужны числа
    pattern = r'\d{1,9}' # берет цифры от 1 до 9
    saraly = re.findall(pattern, s)[0]
    print(saraly)


def main():
    file = open('index.html', 'r', encoding='utf-8').read()
    soup = BeautifulSoup(file, 'lxml')
    # зачастую названия дивов пишутся через - или пробел
    # поэтому лучше привыкнуть использовать словарь, как снизу
    row = soup.find_all('div', {'data-set': 'salary'})
    # есть также метод .parent, который вернет тот блок, где мы ищет что-то опред-ное
    # и уже можно работать конкретно с этим блоком
    Kate = soup.find('div', text='Kate').parent
    # print(Kate)
    # если данные лежат не на поверхности, и их сложно извлечь, можно использовать
    # другой метод
    Alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(Alena)

    # движение по блокам данных, здесь - список сотрудников, осуществляется через два
    # метода, find_next_sibling() и find_previous_sibling()
    Petr = Alena.find_previous_sibling()
    # print(Petr)

    # есть еще фильтрующие функции, будет выше и тут показана их работа
    cw_list = []
    all_people = soup.find_all('div', {'class': 'row'})
    for people in all_people:
        cw = get_copywriter(people)
        if cw:
            cw_list.append(cw)
    #print(cw_list)


    # поиск зп
    salary = soup.find_all('div', {'data-set':'salary'})
    for i in salary:
        get_salary(i.text) # выведет просто цифры, т.к. мы это настроили в ф-и
    # но есть еще вариант использования РВ
    salary = soup.find_all('div', text=re.compile('\d{1,9}'))  # pythex.org
    for i in salary:
        print(i.text) # возвращает просто строчку, т.к. не проходило обработку

    #^ - начало строки
    #$ - конец строки
    #. - любой символ
    #+ - неогран кол-во вхождений
    #'\d' - цифра
    #'\w' - буква, цифра, _

    tw = soup.find_all('div', text=re.compile('\d{^@}'))  # хз, что надо
    for tt in tw:
        print(tt.text)

if __name__ == '__main__':
    main()
