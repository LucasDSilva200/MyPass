import random
import string
import os
from time import sleep
from detectos import detect

from file import clean_file, criar_caminho, ler_arquivo, salvar_arquivo

PATH = detect()
FILEPATH = PATH + "/passwords.txt"


@staticmethod
def create_file():
    if not os.path.exists(PATH):
        criar_caminho(PATH)
        try:
            file = open(FILEPATH)
            file.close()
        except FileNotFoundError:
            clean_file(FILEPATH)


def gerar_senha(tamanho):
    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+*/}{:;.><,'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars)for i in range(tamanho))


def salvar_senha(servico, username, password):
    texto = f"{servico}={username}:{password}"
    salvar_arquivo(FILEPATH, texto)


def listar_senha():
    senhas = ler_arquivo(FILEPATH)
    for senha in senhas:
        print('\n'+senha.strip('\n'))
        sleep(0.5)


def exportar_senha(filesave):
    senhas = ler_arquivo(FILEPATH)
    for senha in senhas:
        texto = senha.strip('\n')
        salvar_arquivo(filesave, texto)


def buscar_senha(pass_query):
    senhas = ler_arquivo(FILEPATH)
    for senha in senhas:
        if pass_query in senha:
            print('\n'+senha.strip('\n'))
            sleep(0.5)


def apagar_registro(registro):
    senhas = ler_arquivo(FILEPATH)
    clean_file(path=PATH)
    for senha in senhas:
        if registro == senha.strip('\n'):
            pass
        else:
            salvar_arquivo(path=FILEPATH, text=senha.strip('\n'))
            sleep(0.5)
