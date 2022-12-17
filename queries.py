import logging
from db import create_database
from detectos import detect


PATH = detect()

DATABASE = create_database(path=PATH)
CURSOR = DATABASE.cursor()


def save_register(site_name, register: dict):
    CURSOR.execute(
        f"INSERT INTO registro VALUES('{site_name}', '{register['url_site']}',"
        + f"'{register['username']}', '{register['password']}')")


def list_register() -> list:
    CURSOR.execute("SELECT * FROM registro")
    return CURSOR.fetchall()


def query_register(site_name) -> list:
    CURSOR.execute(f"SELECT * FROM registro  WHERE nome_site='{site_name}'")
    return CURSOR.fetchall()


def remove_register(site_name, username) -> str:
    try:
        CURSOR.execute("DELETE FROM registro "
                       + f"WHERE nome_site='{site_name}' "
                       + f"AND username='{username}'")
        return 'Done!!!'
    except BaseException as e:
        logging.exception(e)
        return 'Fail!!!'


def modify_register(site_name, register: dict) -> str:
    try:
        CURSOR.execute("UPDATE registro "
                       + f"SET username='{register['username']}',"
                       + f"password='{register['password']}' "
                       + f"WHERE nome_site='{site_name}'")
        return 'Done!!!'
    except BaseException as e:
        logging.exception(e)
        return 'Fail!!!'
