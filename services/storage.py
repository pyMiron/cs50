import sqlite3


class API_Storage:
    conn = '..api_services.sqlite'
    groups = None
    



    def __init__(self, conn):
        self.__conn = sqlite3.connect(f'{conn}')
        self.__cur = self.__conn.cursor()

        self.__cur.execute('CREATE TABLE IF NOT EXIST groups(id int auto_increment primary key, name text)')
        self.__cur.execute('CREATE TABLE IF NOT EXIST users(id int auto_increment primary key, group_id text, telegram_id text, name text, second_name text, created_at text )')
        self.__cur.execute('CREATE TABLE IF NOT EXIST homework(id int auto_increment primary key, telegram_id text, group_id text, name text, description text, group_code text)')

