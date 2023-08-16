#!/usr/bin/env python


import csv
from src.queries import save_register


# path,lines:list


def export_to_csv(path, lines: list):
    columns = [('Nome do site', 'URL', 'Username', 'Password')]
    filepath = path + "/mypass.csv"
    f = open(filepath, 'w', newline='', encoding='utf-8')

    w = csv.writer(f, delimiter=';')

    for coluna in columns:
        w.writerow([coluna[0],
                    coluna[1],
                    coluna[2],
                    coluna[3]])

    for line in lines:
        w.writerow([line[0],
                    line[1],
                    line[2],
                    line[3]])
    print("\nArquivo salvo com sucesso!!!")
    print(f"Local do arquivo {filepath}")
    f.close()


def import_to_csv(path):
    try:
        with open(path, encoding='utf-8') as csv_file:
            register = {}
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    register[row[0]] = {
                        'url_site': row[1],
                        'username': row[2],
                        'password': row[3]
                    }
                    save_register(site_name=row[0],
                                  register=register[row[0]])

                    line_count += 1
            print(f'Processed {line_count} lines.')
    except FileNotFoundError:
        print("Arquivo não encontrado")
