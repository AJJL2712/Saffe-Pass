import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb

from src.auth_service import crear_usuario
from src.register_window import RegisterWindow

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Iniciar Sesión / Registrarse")
        self.on_login_success = on_login_success

        frame = tb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        tb.Label(frame, text="Correo Electrónico:").pack(anchor="w")
        self.email_entry = tb.Entry(frame)
        self.email_entry.pack(fill="x", pady=5)

        tb.Label(frame, text="Contraseña:").pack(anchor="w")
        self.password_entry = tb.Entry(frame, show="*")
        self.password_entry.pack(fill="x", pady=5)

        btn_frame = tb.Frame(frame)
        btn_frame.pack(fill="x", pady=10)

        tb.Button(btn_frame, text="Registrarse", bootstyle="primary", command=self.abrir_registro).pack(side="left", expand=True, fill="x", padx=5)
        tb.Button(btn_frame, text="Continuar", bootstyle="success", command=self.continuar).pack(side="right", expand=True, fill="x", padx=5)

    def abrir_registro(self):
        self.root.withdraw()  # Oculta login
        RegisterWindow(self.root, on_close=self.root.deiconify)

    def continuar(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not email or not password:
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        uid_simulado = email
        self.on_login_success(uid_simulado)
