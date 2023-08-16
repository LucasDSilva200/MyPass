import random
import string
import hashlib
from time import sleep
from src.file import export_to_csv, import_to_csv

from src.queries import modify_register, query_register, \
    remove_register, save_register, list_register, set_user, \
    get_salt, get_hash, get_user_id, verify_user
from src.key import create_key
from src.detectos import detect
REGISTER = {}


def create_hashed_password(salted_pass):
    sha512pass = hashlib.sha512(salted_pass.encode()).hexdigest()
    return sha512pass


def log_in(username, password):
    vUser = verify_user(username=username)
    if vUser:
        salts = get_salt(username=username)
    else:
        return False
    saltpass = salts[0][0]+password
    stored_hash = get_hash(username=username)
    hash_to_compare = create_hashed_password(salted_pass=saltpass)
    if hash_to_compare == stored_hash[0][0]:
        id = get_user_id(username=username, hashpassword=hash_to_compare)
        return True, id[0][0]
    else:
        return False


def create_user(username, password):
    vUser = verify_user(username=username)
    if vUser:
        print("O nome de usuário já existe!!")
        return False
    else:
        salt = create_key(path=detect())
        saltpass = salt+password
        hashpassword = create_hashed_password(salted_pass=saltpass)
        set_user(username=username, salt=salt, hash=hashpassword)
        
    
    

def print_result(result):
    print(f'''
-----------------------------------------------
| Site: {result[0].title()}
| URL: {result[1]}
| Username: {result[2]}
| Password: {result[3]}
-----------------------------------------------
        ''')
    sleep(1)  # import time


def gerar_senha(tamanho):
    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+*/}{:;.><,'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars)for _ in range(tamanho))


def salvar_senha(name_service, url, username, password, id):
    REGISTER[name_service] = {
        'url_site': url,
        'username': username,
        'password': password,
        'id': id
    }
    save_register(site_name=name_service,
                  register=REGISTER[name_service])
    print("Senha salva com sucesso com sucesso!!!")


def listar_senha(id):
    results = list_register(id=id)
    for result in results:
        print_result(result)


def exportar_senha(path, id):
    results = list_register(id=id)
    export_to_csv(path=path, lines=results)


def buscar_senha(pass_query, id):
    results = query_register(pass_query, id=id)
    for result in results:
        print_result(result=result)


def apagar_registro(site_name, username, id):
    msg = remove_register(site_name=site_name, username=username, id=id)
    print('\n'+msg+'\n')


def modificar_registro(site_name, username, password, id):
    REGISTER[site_name] = {
        'url_site': '',
        'username': username,
        'password': password,
        'id': id
    }
    msg = modify_register(site_name=site_name, register=REGISTER[site_name])
    print('\n'+msg+'\n')


def importar_senhas(filepath):

    import_to_csv(filepath)
