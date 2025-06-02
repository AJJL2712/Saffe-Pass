import json
from encryption import cifrar, descifrar, cargar_clave

RUTA_ARCHIVO = "data/passwords.json"

class PasswordManager:
    def __init__(self):
        self.clave = cargar_clave()
        self.passwords = self._cargar_passwords()

    def _cargar_passwords(self):
        try:
            with open(RUTA_ARCHIVO, "r") as f:
                data_cifrada = json.load(f)
            # Descifrar cada contraseña
            passwords = {}
            for etiqueta, pwd_cifrada_str in data_cifrada.items():
                pwd_cifrada_bytes = pwd_cifrada_str.encode('utf-8')
                pwd_descifrada = descifrar(pwd_cifrada_bytes, self.clave)
                passwords[etiqueta] = pwd_descifrada
            return passwords
        except FileNotFoundError:
            return {}

    def guardar_passwords(self):
        # Cifrar cada contraseña antes de guardar
        data_cifrada = {}
        for etiqueta, pwd in self.passwords.items():
            pwd_cifrada = cifrar(pwd, self.clave)
            data_cifrada[etiqueta] = pwd_cifrada.decode('utf-8')
        with open(RUTA_ARCHIVO, "w") as f:
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

# Prueba rápida
if __name__ == "__main__":
    pm = PasswordManager()
    pm.agregar_password("Correo", "SecurePassword123!")
    print("Contraseña guardada para 'Correo'.")
    print("Listado:", pm.listar_etiquetas())
    print("Contraseña para 'Correo':", pm.obtener_password("Correo"))
