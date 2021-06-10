import psycopg2
from credentials import *


def get_id():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT id FROM cripta_bot;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def insert_into_db(data):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    chat_id = data
    cursor.execute(f'INSERT INTO cripta_bot (id) VALUES ({chat_id});')
    cursor.execute('COMMIT;')
    cursor.close()
    conn.close()
