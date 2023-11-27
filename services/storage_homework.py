from storage import API_Storage
import sqlite3


class StorageHomework:
    def __init__(self):
        self.__conn = sqlite3.connect(f'{API_Storage.conn}')
        self.__cur = self.__conn.cursor()

    def getByID(self, id):
        self.__cur.execute(
            f'SELECT * FROM homework WHERE id = "{id}"'
        )
        result = self.__cur.fetchone()
        return result

    def getItemsByAll(self):
        self.__cur.execute(
            f'SELECT * FROM homework'
        )
        result = self.__cur.fetchall()
        return result

    def create(self, id, telegram_id, group_id, name, description, group_code):
        self.__cur.execute(
            'INSERT INTO homework(id, telegram_id, group_id, name, description, group_code) VALUES("%","%","%","%","%","%")'%(id, telegram_id, group_id, name, description, group_code)
        )

    def update(self, name, new_name, id):
        self.__cur.execute(
            f'UPDATE homework SET "{name}" = "{new_name}" WHERE id = "{id}"'
        )

    def delete(self, id):
        self.__cur.execute(
            f"DELETE FROM homework WHERE id = '{id}'"
        )