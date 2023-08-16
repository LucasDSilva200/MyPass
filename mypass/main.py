#!/usr/bin/env python


import colorama
from colorama import Fore
from src.util import apagar_registro, buscar_senha,\
    exportar_senha, gerar_senha, \
    importar_senhas, listar_senha,\
    modificar_registro, salvar_senha, create_user, log_in
from src.queries import DATABASE, PATH
from src.menus import print_not_logged_menu, print_main_menu
from getpass import getpass

colorama.init(autoreset=True)


def main():
    logged = False
    id = ''
    while not logged:
        print_not_logged_menu()

        try:
            option = int(input(f"{Fore.YELLOW}MyPass>:{Fore.RESET} "))
        except ValueError:
            print("Opção inválida")
        else:
            match option:
                case 1:
                    username = input("Username: ")
                    password = getpass(prompt="Senha: ")
                    logged, id = log_in(username=username, password=password)
                case 2:
                    username = input("Username: ")
                    password = getpass(prompt="Senha: ")
                    confirm_password = getpass(prompt="Confirme a senha: ")
                    while confirm_password != password:
                        print("As senhas não são iguais")
                        password = getpass(prompt="Senha: ")
                        confirm_password = getpass(prompt="COnfirme a senha: ")
                    create_user(username=username, password=password)
                case 0:
                    print("Até mais!!!\n")
                    break
        DATABASE.commit()

    while logged:
        print_main_menu()
        try:
            option = int(input(f"{Fore.YELLOW}MyPass>:{Fore.RESET} "))

        except ValueError:
            print("Opção inválida")
        else:
            match option:
                case 1:
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
                                     username=user, password=senha, id=id)
                    else:
                        continue

                case 2:
                    print(f"\n{Fore.YELLOW}Listando as senhas salvas:\n")
                    print(Fore.LIGHTGREEN_EX+"-"*50)
                    listar_senha(id=id)
                    print(Fore.LIGHTGREEN_EX+"-"*50)
                    print("\n")
                case 3:
                    servico = input("O nome do site: ").lower()
                    url = input("A url do site: ")
                    user = input("O seu usuario: ")
                    password = input("a senha: ")
                    salvar_senha(name_service=servico, url=url,
                                 username=user, password=password, id=id)

                case 4:
                    exportar_senha(PATH, id=id)
                case 5:
                    print("Informe o caminho do arquivo .csv ")
                    filepath = input("Path> ")
                    importar_senhas(filepath=filepath)
                case 6:
                    perfil = input(
                        "Digite o nome do site que deseja "
                        + "pesquisar: ").lower()
                    buscar_senha(pass_query=perfil, id=id)
                case 7:
                    site = input("Qual é o nome do site que deseja"
                                 + "alterar as credenciais: ")
                    user = input("O seu usuario: ")
                    password = input("a senha: ")
                    modificar_registro(site_name=site,
                                       username=user, password=password, id=id)
                case 8:
                    site = input(
                        "Digite o nome do site para ser excluido"
                        + "> ")
                    user = input("Digite o user que deseja apagar> ")
                    apagar_registro(site_name=site, username=user, id=id)

                case 0:
                    DATABASE.close()
                    break
                case _:
                    print("Opção inválida")

            DATABASE.commit()


if __name__ == '__main__':
    main()
