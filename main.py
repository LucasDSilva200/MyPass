#!/usr/bin/env python


import colorama
from colorama import Fore
from util import apagar_registro, buscar_senha, \
    exportar_senha, gerar_senha, \
    listar_senha, salvar_senha,\
    modificar_registro
from queries import DATABASE, PATH

colorama.init(autoreset=True)


def print_menu():
    print('''
-------------------------------------
|Escolha uma das opções abaixo      |
-------------------------------------
| 1 - Para gerar senha              |
| 2 - Para listar as senhas salvas  |
| 3 - Para salvar uma nova senha    |
| 4 - Exportar dados                |
| 5 - Pesquisar                     |
| 6 - Modificar Registro            |
| 7 - Apagar registro               |
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
        else:
            if option == 1:
                try:
                    tamanho = int(input("Digite o tamanho da senha: "))
                except ValueError:
                    tamanho = 15
                senha = gerar_senha(tamanho)
                print(Fore.GREEN+senha)
                save = input("Salvar a senha gerada ?(Y or n)> ")
                if save.lower() == 'y':
                    servico = input("O nome do site: ").lower()
                    url = input("A url do site: ")
                    user = input("O seu usuario: ")
                    salvar_senha(name_service=servico, url=url,
                                 username=user, password=senha)
                else:
                    continue

            elif option == 2:
                print(f"\n{Fore.YELLOW}Listando as senhas salvas:\n")
                print(Fore.LIGHTGREEN_EX+"-"*50)
                listar_senha()
                print(Fore.LIGHTGREEN_EX+"-"*50)
                print("\n")
            elif option == 3:
                servico = input("O nome do site: ").lower()
                url = input("A url do site: ")
                user = input("O seu usuario: ")
                password = input("a senha: ")
                salvar_senha(name_service=servico, url=url,
                             username=user, password=password)

            elif option == 4:
                exportar_senha(PATH)
            elif option == 5:
                perfil = input(
                    "Digite o nome do site que deseja "
                    + "pesquisar: ").lower()
                buscar_senha(pass_query=perfil)
            elif option == 6:
                site = input("Qual é o nome do site que deseja"
                             + "alterar as credenciais: ")
                user = input("O seu usuario: ")
                password = input("a senha: ")
                modificar_registro(site_name=site,
                                   username=user, password=password)
            elif option == 7:
                site = input(
                    "Digite o nome do site para ser excluido"
                    + "> ")
                user = input("Digite o user que deseja apagar> ")
                apagar_registro(site_name=site, username=user)

            elif option == 0:
                DATABASE.close()
                break
            else:
                print("Opção inválida")

            DATABASE.commit()


if __name__ == '__main__':
    main()
