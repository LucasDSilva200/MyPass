import random
import string
import os
from time import sleep
from detectos import detect

from file import criar_caminho, ler_arquivo, salvar_arquivo

path = detect()


def gerar_senha(tamanho):
    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+*/}{:;.><,'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars)for i in range(tamanho))


def salvar_senha(servico, username, password):
    global path
    if not os.path.exists(path):
        criar_caminho(path)
    texto = f"{servico}={username}:{password}"
    filepath = path+"/passwords.txt"
    salvar_arquivo(filepath, texto)


def listar_senha():
    global path
    filepath = path+"/passwords.txt"
    senhas = ler_arquivo(filepath)
    for senha in senhas:
        print(senha.strip('\n'))
        sleep(0.5)



def exportar_senha(filesave):
    global path
    filepath = path +"/passwords.txt"
    senhas = ler_arquivo(filepath)
    for senha in senhas:
        texto = senha.strip('\n')
        salvar_arquivo(filesave,texto)


