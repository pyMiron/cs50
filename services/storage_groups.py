from storage import API_Storage
import sqlite3


class StorageGroups:
    def __init__(self, cur):
        self.__conn = sqlite3.connect(f'{API_Storage.conn}')
        self.__cur = self.__conn.cursor()

    def getByID(self, id):
        self.__cur.execute(
            f'SELECT * FROM groups WHERE id = "{id}"'
        )
        result = self.__cur.fetchone()
        return result

    def getItemsByAll(self):
        self.__cur.execute(
            f'SELECT * FROM groups'
        )
        result = self.__cur.fetchall()
        return result

    def create(self, id, name):
        self.__cur.execute(
            'INSERT INTO groups(id, name) VALUES ("%","%")' % (id, name)
        )

    def update(self, name, new_name, id):
        self.__cur.execute(
            f'UPDATE groups SET "{name}" = "{new_name}" WHERE id = "{id}"'
        )

    def delete(self, id):
        self.__cur.execute(
            f"DELETE FROM groups WHERE id = '{id}'"
        )
