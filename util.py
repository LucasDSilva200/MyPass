import random
import string
import os
from time import sleep
from detectos import detect

from file import clean_file, criar_caminho, ler_arquivo, salvar_arquivo

PATH = detect()


def gerar_senha(tamanho):
    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+*/}{:;.><,'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars)for i in range(tamanho))


def salvar_senha(servico, username, password):
    if not os.path.exists(PATH):
        criar_caminho(PATH)
    texto = f"{servico}={username}:{password}"
    filepath = PATH+"/passwords.txt"
    salvar_arquivo(filepath, texto)


def listar_senha():
    filepath = PATH+"/passwords.txt"
    senhas = ler_arquivo(filepath)
    for senha in senhas:
        print('\n'+senha.strip('\n'))
        sleep(0.5)


def exportar_senha(filesave):
    filepath = PATH + "/passwords.txt"
    senhas = ler_arquivo(filepath)
    for senha in senhas:
        texto = senha.strip('\n')
        salvar_arquivo(filesave, texto)


def buscar_senha(pass_query):
    filepath = PATH+"/passwords.txt"
    senhas = ler_arquivo(filepath)
    for senha in senhas:
        if pass_query in senha:
            print('\n'+senha.strip('\n'))
            sleep(0.5)


def apagar_registro(registro):
    filepath = PATH+"/passwords.txt"
    senhas = ler_arquivo(filepath)
    clean_file(path=filepath)
    for senha in senhas:
        if registro == senha.strip('\n'):
            pass
        else:
            salvar_arquivo(path=filepath, text=senha.strip('\n'))
            sleep(0.5)
