import csv
from peewee import *

# устанавливает связь м/у ОРМ (пиви) м БД
# класс в переменной db = он лежит в пиви
db = PostgresqlDatabase(database='testdb', user='postgres', password='A8nDIVDh23', host='localhost')


# сейчас создадим класс, который будет представлять собой таблицу из БД с данными
# Model also was imported from PeeWee
class Coin(Model):
    coin_name = CharField()
    coin_symbol = CharField()
    coin_link = TextField()
    coin_price = CharField()

    # связываем класс с БД
    class Meta():
        database = db


def main():

    db.connect()
    # принимает список таблиц, которые надо создать в БД, у нас только одна таблица. Ее поля описаны в классе выше
    db.create_tables([Coin])

    with open('cmc4.csv', 'r', encoding='utf-8') as file:
        order = ['coin_name', 'coin_symbol', 'coin_link', 'coin_price']
        reader = csv.DictReader(file, fieldnames=order)
        coins = list(reader)

        # есть несколько вариантов записи данных,самый плохой показывать не буду, начну с более менее норм
        # (**row) подсвечен, но все сработало, данные записались
        with db.atomic():
            #for row in coins:
            #    Coin.create(**row)

            # другой вариант еще более быстрый, там также будет через with db.atomic():
            # тут данные подаются по кускам, что позволяет сократить количество циклов
            for index in range(0, len(coins), 10):
                Coin.insert_many(coins[index:index+10]).execute()

    # надо еще изучить,как делать дамп БД из иде,

if __name__ == '__main__':
    main()
