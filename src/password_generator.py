# Módulo con funciones para generar contraseñas
import random
import string

def generar_contraseña(longitud=12):
    """
    Genera una contraseña segura que incluye letras mayúsculas,
    minúsculas, números y símbolos.

    :param longitud: longitud de la contraseña (mínimo 8 recomendado)
    :return: contraseña como string
    """
    if longitud < 8:
        raise ValueError("La longitud mínima recomendada es 8 caracteres")

    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Prueba rápida
if __name__ == "__main__":
    print("Contraseña generada:", generar_contraseña(16))
