from src.gui import PasswordManagerGUI
from src.login_window import LoginWindow
import ttkbootstrap as tb

# Crear una única ventana principal
ventana = tb.Window(themename="flatly")

def iniciar_aplicacion(uid):
    # Limpiar todos los widgets actuales (login)
    for widget in ventana.winfo_children():
        widget.destroy()
    # Iniciar el gestor dentro de la misma ventana
    PasswordManagerGUI(ventana, uid)

if __name__ == "__main__":
    LoginWindow(ventana, on_login_success=iniciar_aplicacion)
    ventana.mainloop()
