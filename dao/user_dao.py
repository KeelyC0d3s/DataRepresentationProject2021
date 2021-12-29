import mysql.connector
import bcrypt
from dao import dbconfig as cfg
from model.user_details import UserDetails


class UserDao:
    _db = ""

    def __init__(self):
        self._connect_to_db()

    def _connect_to_db(self):
        self._db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def _get_cursor(self):
        if not self._db.is_connected():
            self._connect_to_db()
        return self._db.cursor()

    def create_user(self, user_details: UserDetails):
        cursor = self._get_cursor()

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(str.encode(user_details.password, 'utf-8'), salt)

        sql = "Insert into user_details (name, username, email_address, salt, password) values (%s, %s, %s, %s, %s)"
        values = (user_details.name, user_details.username, user_details.email_address, salt, hashed_password)
        cursor.execute(sql, values)

        self._db.commit()

        cursor.close()

    def get_user_by_id(self, user_id: int):
        cursor = self._get_cursor()
        sql = "Select * from user_details where id = %s"
        values = (user_id,)
        cursor.execute(sql, values)

        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None
        else:
            return UserDetails(result[0], result[1], result[2], result[3], result[5])

    def get_user_by_username(self, username: str):
        cursor = self._get_cursor()
        sql = "Select * from user_details where username = %s"
        values = (username,)
        cursor.execute(sql, values)

        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None
        else:
            return UserDetails(result[0], result[1], result[2], result[3], result[5])


user_dao = UserDao()
