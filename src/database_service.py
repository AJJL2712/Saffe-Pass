from src.firebase_init import db
from src.encryption import cifrar, descifrar, cargar_clave

def guardar_contraseña(uid, servicio, usuario, contrasena):
    clave = cargar_clave()
    contrasena_cifrada = cifrar(contrasena, clave).decode()
    doc_ref = db.collection('usuarios').document(uid).collection('passwords').document(servicio)
    doc_ref.set({
        'usuario': usuario,
        'contrasena': contrasena_cifrada
    })

def leer_contraseñas(uid):
    clave = cargar_clave()
    passwords_ref = db.collection('usuarios').document(uid).collection('passwords')
    docs = passwords_ref.stream()
    resultados = {}
    for doc in docs:
        datos = doc.to_dict()
        contrasena_cifrada = datos["contrasena"].encode()
        resultados[doc.id] = {
            "usuario": datos["usuario"],
            "contrasena": descifrar(contrasena_cifrada, clave)
        }
    return resultados
