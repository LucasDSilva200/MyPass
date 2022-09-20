import os


def criar_caminho(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def salvar_arquivo(path, text):
    with open(path, 'a+')as file:
        file.write(text)
        file.write("\n")


def ler_arquivo(path):
    with open(path, 'r+')as file:
        linhas = file.readlines()
    return linhas
