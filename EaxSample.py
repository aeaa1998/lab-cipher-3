from Crypto.Cipher import AES

class EAX(object):
    def __init__(self, key):
        self.key = str.encode(key)
        self.permision = False

    def encrypt(self, plaintext):
        cif = AES.new(self.key, AES.MODE_EAX)
        self.nonce = cif.nonce
        self.permision = True
        return cif.encrypt_and_digest(str.encode(plaintext))

    def decrypt(self, ciphertext, tag):
        if self.permision:
            cif = AES.new(self.key, AES.MODE_EAX, self.nonce)
            plaintext = cif.decrypt(ciphertext).decode('utf-8')
            try:
                cif.verify(tag)
                return plaintext
            except:
                print("El mensaje se corrompio")
        else:
            return 'Tienes que encriptar primero'


if __name__ == '__main__':
    print('Bienvenido al programa')
    key = input('Ingrese la llave con la que va realizar las operaciones: ')
    menu = '\nMenu:\n   1. Encriptar\n   2. Desencriptar\n   3. Salir'
    my_eax = EAX(key)
    op = ''
    ciphertext = ''
    tag = ''
    while op != 3:
        print(menu)
        bandera = True
        while bandera:
            try:
                op = int(input('Ingresa tu opción que deseas: '))
                bandera = False
            except:
                print('Ingrese valores correctos')

        if op == 1:
            ciphertext, tag = my_eax.encrypt(input('Ingrese el mensaje a encriptar: '))
        elif op == 2:
            res = ''
            while res != 'y' and res != 'n':
                res = input('Desea desencriptar el mensaje que encriptó anteriormente?: ').lower()
            if res == 'y':
                print(my_eax.decrypt(ciphertext, tag))
            else:
                ciphertext = input('Ingrese el texto cifrado: ')
                tag = input('Ingrese el tag: ')
                print(my_eax.decrypt(ciphertext, tag))
        elif op == 3:
            print('Hasta luego')
        else:
            print("Ingrese valores válidos")
