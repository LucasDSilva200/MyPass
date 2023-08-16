#!/usr/bin/env python


import logging
from src.db import create_database
from src.detectos import detect


PATH = detect()

DATABASE = create_database(path=PATH)
CURSOR = DATABASE.cursor()


def save_register(site_name, register: dict):
    CURSOR.execute(
        "INSERT INTO registro(nome_site, url_site,"
        + "username, password, usuario_id) SELECT "
        + "?,?,"
        + "?,?,? "
        + "WHERE NOT EXISTS ("
        + "SELECT * FROM registro "
        + "WHERE nome_site = ? "
        + "AND url_site = ? "
        + "AND username = ? "
        + "AND password = ? "
        + "AND usuario_id = ?);",
        (site_name, register['url_site'], register['username'],
         register['password'], register['id'], site_name, register['url_site'],
         register['username'], register['password'], register['id']))


def list_register(id) -> list:
    CURSOR.execute("SELECT * FROM registro WHERE usuario_id = ?",
                   (id,))
    return CURSOR.fetchall()


def query_register(site_name, id) -> list:
    CURSOR.execute(
        "SELECT * FROM registro  WHERE nome_site=? AND usuario_id=?",
        (site_name, id))
    return CURSOR.fetchall()


def remove_register(site_name, username, id) -> str:
    try:
        CURSOR.execute("DELETE FROM registro "
                       + "WHERE nome_site=? "
                       + "AND username=?, AND usuario_id=?",
                       (site_name, username, id))
        return 'Done!!!'
    except BaseException as e:
        logging.exception(e)
        return 'Fail!!!'


def modify_register(site_name, register: dict) -> str:
    try:
        CURSOR.execute("UPDATE registro "
                       + "SET username=?,"
                       + "password=? "
                       + "WHERE nome_site=? AND usuario_id=?",
                       (register["username"],
                        register["password"],
                        site_name, register['id']))
        return 'Done!!!'
    except BaseException as e:
        logging.exception(e)
        return 'Fail!!!'


def get_salt(username):
    CURSOR.execute("SELECT salt FROM usuario WHERE username = ?",
                   (username,))
    return CURSOR.fetchall()


def get_hash(username):
    CURSOR.execute("SELECT hash FROM usuario WHERE username= ?", (username,))
    return CURSOR.fetchall()

def verify_user(username):
    CURSOR.execute("SELECT username FROM usuario WHERE username= ?",(username,))
    if CURSOR.fetchall():
        return True
    else:
        return False 

def get_user_id(username, hashpassword):
    CURSOR.execute(
        "SELECT id FROM usuario WHERE username= ? AND hash= ?",
        (username,
         hashpassword))
    return CURSOR.fetchall()


def set_user(username, salt, hash):
    CURSOR.execute(
        "INSERT INTO usuario(username, salt,"
        + "hash) SELECT "
        + " ?, ?, ?"
        + "WHERE NOT EXISTS ("
        + "SELECT * FROM usuario "
        + "WHERE username = ?);", (username, salt, hash, username))
