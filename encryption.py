# Módulo para cifrar y descifrar
from cryptography.fernet import Fernet

# Generar y guardar una clave segura la primera vez
def generar_clave():
    clave = Fernet.generate_key()
    with open("data/key.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    return clave

# Cargar clave desde archivo
def cargar_clave():
    return open("data/key.key", "rb").read()

# Función para cifrar texto
def cifrar(texto, clave):
    f = Fernet(clave)
    texto_cifrado = f.encrypt(texto.encode())
    return texto_cifrado

# Función para descifrar texto
def descifrar(texto_cifrado, clave):
    f = Fernet(clave)
    texto_descifrado = f.decrypt(texto_cifrado).decode()
    return texto_descifrado

# Ejemplo de uso rápido
if __name__ == "__main__":
    try:
        clave = cargar_clave()
    except FileNotFoundError:
        clave = generar_clave()
        print("Clave generada y guardada en data/key.key")

    texto_original = "contraseña_segura"
    texto_cifrado = cifrar(texto_original, clave)
    print("Texto cifrado:", texto_cifrado)
    print("Texto descifrado:", descifrar(texto_cifrado, clave))
