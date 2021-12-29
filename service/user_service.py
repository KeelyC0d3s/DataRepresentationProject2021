import bcrypt
from dao.user_dao import user_dao

from model.user_details import UserDetails


def get_user_by_id(user_id: int):
    return user_dao.get_user_by_id(user_id)


def get_user_by_user_name(user_name: str):
    return user_dao.get_user_by_username(user_name)


def register_new_user(user_details: UserDetails):
    user_dao.create_user(user_details)


def user_exists(user_name: str) -> bool:
    return user_dao.get_user_by_username(user_name) is not None


def try_login_user(user_name: str, user_password: str) -> bool:
    if not user_exists(user_name):
        print(f'user does not exist: {user_name}')
        return False

    user = user_dao.get_user_by_username(user_name)
    return bcrypt.checkpw(str.encode(user_password, 'utf-8'), str.encode(user.password, 'utf-8'))
