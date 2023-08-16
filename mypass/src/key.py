import string
import random


def create_key(path):
    key_path = path+"/key.txt"

    try:
        with open(key_path, "r") as file:
            key = file.readline().strip()
        return key
    except FileNotFoundError:
        key_file = path+"/key.txt"
        chars = string.digits
        rnd = random.SystemRandom()
        key = ''.join(rnd.choice(chars)for _ in range(10))
        with open(key_file, "w+") as file:
            file.write(key)
        return key
