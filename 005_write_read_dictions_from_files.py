import csv


def write_csv(data):
    with open('names.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['name'],
            data['surname'],
            data['age']
        ))


# т.к. словари рандомно чередуют порядок внутренностей, то попать в предыдущую ф-ю они могут тоже криво
# поэтому надо использовать ф-ю внизу, кот так и призывается для работы со словарями
# хот верхнее тоже норм записывает, хуй его знает
def write_csv2(data):
    with open('names.csv', 'a', encoding='utf-8', newline='') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def main():
    dct1 = {
        'name': 'Alex',
        'surname': 'Munroe',
        'age': 19
    }

    dct2 = {
        'name': 'Alena',
        'surname': 'Munroe',
        'age': 18
    }

    dct3 = {
        'name': 'Kesha',
        'surname': 'Baldurson',
        'age': 20
    }

    # lst = [dct1, dct2, dct3]
    # for el in lst:  # т.к. у нас список, то для каждого элемента отдельно вызываем
    #    if el != '':
    #        write_csv2(el)
    #    else:
    #        print('emply line')  # тут идет запись в CSV

    with open('plugins2.csv', 'r') as file:
        fieldnames = ['name', 'rating', 'author', 'link']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in reader:
            print(row['name'])

if __name__ == '__main__':
    main()
