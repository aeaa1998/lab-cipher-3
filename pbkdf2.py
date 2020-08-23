import os, binascii
from backports.pbkdf2 import pbkdf2_hmac
from random import choice
import string

def generate_derivation(password):
    slt = binascii.unhexlify(''.join([choice(string.hexdigits) for x in range(32)]))
    key = pbkdf2_hmac('sha256', str.encode(password), slt, 100000, 32)
    return binascii.hexlify(key).decode('utf-8')

if __name__ == '__main__':
    print('Bienvenido al programa')
    op = 0
    while op != 2:
        op = 0
        while op != 1 and op != 2:
            try:
                op = int(input('\nMenu:\n   1. Derivar una contraseña\n   2. Salir\n Ingrese una opción: '))
            except:
                print('Ingrese solo números')
        print(generate_derivation(input('Ingrese una contraseña: ')) if op == 1 else 'Hasta luego')