import sqlite3
import os


def criar_caminho(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def create_database(path):
    try:

        banco = sqlite3.connect(path+'/mypass.db')
    except sqlite3.OperationalError:

        if not os.path.exists(path):
            criar_caminho(path)
        banco = sqlite3.connect(path+'/mypass.db')
        create_tables(banco)

    return banco


def create_tables(db):
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE registro(
            nome_site text,
            url_site text,
            username text,
            password text
    )
    ''')
