from storage import API_Storage
import sqlite3


class StorageUsers:
    def __init__(self):
        self.__conn = sqlite3.connect(f'{API_Storage.conn}')
        self.__cur = self.__conn.cursor()

    def getByID(self, id):
        self.__cur.execute(
            f'SELECT * FROM users WHERE id = "{id}"'
        )
        result = self.__cur.fetchone()
        return result

    def getItemsByAll(self):
        self.__cur.execute(
            f'SELECT * FROM users'
        )
        result = self.__cur.fetchall()
        return result

    def create(self, id , group_id , telegram_id , name , second_name , created_at):
        self.__cur.execute(
            'INSERT INTO users(id, group_id, telegram_id, name, second_name, created_at) VALUES ("%","%","%","%","%","%")' % (id , group_id , telegram_id , name , second_name , created_at)
        )

    def update(self, name, new_name, id):
        self.__cur.execute(
            f'UPDATE users SET "{name}" = "{new_name}" WHERE id = "{id}"'
        )

    def delete(self, id):
        self.__cur.execute(
            f"DELETE FROM users WHERE id = '{id}'"
        )
