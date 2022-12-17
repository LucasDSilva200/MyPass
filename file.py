import csv

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
