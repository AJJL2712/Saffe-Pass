from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError

def crear_usuario(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print("Usuario creado:", user.uid)
        return user.uid
    except EmailAlreadyExistsError:
        print("⚠️ El correo ya está registrado.")
        return None
    except Exception as e:
        print("Error al crear usuario:", e)
        return None
