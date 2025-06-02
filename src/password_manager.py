import os
import json
from encryption import cifrar, descifrar, cargar_clave, generar_clave

# Ruta segura al archivo JSON
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RUTA_ARCHIVO = os.path.join(DATA_DIR, "passwords.json")

class PasswordManager:
    def __init__(self):
        generar_clave()  # Garantiza que exista la clave
        self.clave = cargar_clave()
        self.passwords = self._cargar_passwords()

    def _cargar_passwords(self):
        try:
            with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
                data_cifrada = json.load(f)
            passwords = {}
            for etiqueta, pwd_cifrada_str in data_cifrada.items():
                pwd_cifrada_bytes = pwd_cifrada_str.encode("utf-8")
                pwd_descifrada = descifrar(pwd_cifrada_bytes, self.clave)
                passwords[etiqueta] = pwd_descifrada
            return passwords
        except FileNotFoundError:
            return {}

    def guardar_passwords(self):
        data_cifrada = {}
        for etiqueta, pwd in self.passwords.items():
            pwd_cifrada = cifrar(pwd, self.clave)
            data_cifrada[etiqueta] = pwd_cifrada.decode("utf-8")
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(data_cifrada, f, indent=4)

    def agregar_password(self, etiqueta, password):
        self.passwords[etiqueta] = password
        self.guardar_passwords()

    def obtener_password(self, etiqueta):
        return self.passwords.get(etiqueta)

    def eliminar_password(self, etiqueta):
        if etiqueta in self.passwords:
            del self.passwords[etiqueta]
            self.guardar_passwords()
            return True
        return False

    def listar_etiquetas(self):
        return list(self.passwords.keys())

    def obtener_todo(self):
        return self.passwords

# Solo para prueba directa
if __name__ == "__main__":
    pm = PasswordManager()
    pm.agregar_password("Github", "clave123!")
    print(pm.listar_etiquetas())
    print(pm.obtener_password("Github"))
