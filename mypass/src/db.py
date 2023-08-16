#!/usr/bin/env python


import sqlite3
import os


def criar_caminho(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def create_database(path):
    try:
        if not os.path.exists(path):
            criar_caminho(path)

        banco = sqlite3.connect(path+'/mypass.db')
        create_tables(banco)

    except sqlite3.OperationalError:
        banco = sqlite3.connect(path+'/mypass.db')

    return banco


def create_tables(db):
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE usuario(
            id INTEGER PRIMARY KEY,
            username TEXT,
            salt TEXT,
            hash TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE registro(
            nome_site text,
            url_site TEXT,
            username TEXT,
            password TEXT,
            usuario_id INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
    )
    ''')
