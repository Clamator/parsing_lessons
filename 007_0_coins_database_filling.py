file = open('cmc4.csv', mode='r')

import psycopg2

conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
cur = conn.cursor()

for x in range(100):
    text = file.readline()
    cur.execute('insert into coins (coin_name, coin_symbol, coin_link, coin_price) values (%s, %s, %s, %s)',
                text.split(','))
    conn.commit()
