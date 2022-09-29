#!/usr/bin/env python


import colorama
from colorama import Fore
from util import exportar_senha, gerar_senha, listar_senha, salvar_senha


colorama.init(autoreset=True)


while True:
    print("-"*40)
    print("Escolha uma das opções abaixo")
    print("g - para gerar senha")
    print("l -  para listar as senhas salvas")
    print("s - para salvar uma nova senha")
    print("x - exportar a senha")
    print("e - para sair")
    print("-"*40)
    menu = input(f"{Fore.YELLOW}MyPass>:{Fore.RESET} ")
    if menu == 'g':
        try:
            tamanho = int(input("Digite o tamanho da senha: "))
        except ValueError:
            tamanho = 8
        senha = gerar_senha(tamanho)
        print(Fore.GREEN+senha)
    elif menu == 's':
        servico = input("O nome do site: ")
        user = input("O seu usuario: ")
        password = input("a senha: ")
        salvar_senha(servico, user, password)

    elif menu == 'l':
        print(f"\n{Fore.YELLOW}Listando as senhas salvas:\n")
        print(Fore.LIGHTGREEN_EX+"-"*40)
        listar_senha()
        print(Fore.LIGHTGREEN_EX+"-"*40)
        print("\n")

    elif menu == 'x':
        filepath = input("Digite o caminho do arquivo que deseja criar: ")
        exportar_senha(filepath)
    elif menu == 'e':
        break
    else:
        print("Opção inválida")
