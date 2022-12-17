import random
import string
from time import sleep
from file import export_to_csv

from queries import modify_register, query_register, remove_register,\
    save_register, list_register

REGISTER = {}


def print_result(result):
    print(f'''
-----------------------------------------------
| Site: {result[0]}
| URL: {result[1]}
| Username: {result[2]}
| Password: {result[3]}
-----------------------------------------------
        ''')
    sleep(1)  # import time


def gerar_senha(tamanho):
    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+*/}{:;.><,'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars)for i in range(tamanho))


def salvar_senha(name_service, url, username, password):
    REGISTER[name_service] = {
        'url_site': url,
        'username': username,
        'password': password
    }
    save_register(site_name=name_service,
                  register=REGISTER[name_service])
    print("Senha salva com sucesso com sucesso!!!")


def listar_senha():
    results = list_register()
    for result in results:
        print_result(result)


def exportar_senha(path):
    results = list_register()
    export_to_csv(path=path, lines=results)


def buscar_senha(pass_query):
    results = query_register(pass_query)
    for result in results:
        print_result(result=result)


def apagar_registro(site_name, username):
    msg = remove_register(site_name=site_name, username=username)
    print('\n'+msg+'\n')


def modificar_registro(site_name, username, password):
    REGISTER[site_name] = {
        'url_site': '',
        'username': username,
        'password': password
    }
    msg = modify_register(site_name=site_name, register=REGISTER[site_name])
    print('\n'+msg+'\n')
