import os
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KEY_PATH = os.path.join(DATA_DIR, "key.key")

def generar_clave():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(KEY_PATH):
        clave = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(clave)
        return clave
    return cargar_clave()

def cargar_clave():
    return open(KEY_PATH, "rb").read()

def cifrar(texto, clave):
    return Fernet(clave).encrypt(texto.encode())

def descifrar(texto_cifrado, clave):
    return Fernet(clave).decrypt(texto_cifrado).decode()

if __name__ == "__main__":
    clave = generar_clave()
    texto_original = "contraseña_segura"
    texto_cifrado = cifrar(texto_original, clave)
    print("Texto cifrado:", texto_cifrado)
    print("Texto descifrado:", descifrar(texto_cifrado, clave))
