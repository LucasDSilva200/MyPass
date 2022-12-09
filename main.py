#!/usr/bin/env python


import colorama
from colorama import Fore
from util import apagar_registro, buscar_senha, exportar_senha, gerar_senha, listar_senha, salvar_senha


colorama.init(autoreset=True)


def print_menu():
    print('''
-------------------------------------
|Escolha uma das opções abaixo      |
-------------------------------------
| 1 - Para gerar senha              |
| 2 - Para listar as senhas salvas  |
| 3 - Para salvar uma nova senha    |
| 4 - Exportar a senha              |
| 5 - Pesquisar                     |
| 6 - Apagar registro               |
| 0 - Para sair                     |
-------------------------------------
    ''')


def main():
    while True:
        print_menu()
        try:
            option = int(input(f"{Fore.YELLOW}MyPass>:{Fore.RESET} "))
        except ValueError:
            print("Opção inválida")
            main()
        if option == 1:
            try:
                tamanho = int(input("Digite o tamanho da senha: "))
            except ValueError:
                tamanho = 8
            senha = gerar_senha(tamanho)
            print(Fore.GREEN+senha)

        elif option == 2:
            print(f"\n{Fore.YELLOW}Listando as senhas salvas:\n")
            print(Fore.LIGHTGREEN_EX+"-"*40)
            listar_senha()
            print(Fore.LIGHTGREEN_EX+"-"*40)
            print("\n")
        elif option == 3:
            servico = input("O nome do site: ")
            user = input("O seu usuario: ")
            password = input("a senha: ")
            salvar_senha(servico, user, password)

        elif option == 4:
            filepath = input("Digite o caminho do arquivo que deseja criar: ")
            exportar_senha(filepath)
        elif option == 5:
            perfil = input(
                "Digite o nome de usuário ou o site que deseja pesquisar: ")
            buscar_senha(pass_query=perfil)
        elif option == 6:
            perfil = input(
                "Digite o registro comple para ser excluido (site=user:senha)> ")
            apagar_registro(registro=perfil)
        elif option == 0:
            break
        else:
            print("Opção inválida")


if __name__ == '__main__':
    main()
