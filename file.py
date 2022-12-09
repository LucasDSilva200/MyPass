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


def clean_file(path):
    with open(path, 'w+')as file:
        file.write("")


def ler_arquivo(path):
    with open(path, 'r+')as file:
        linhas = file.readlines()
    return linhas
