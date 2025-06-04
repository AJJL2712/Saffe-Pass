import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb

from src.auth_service import crear_usuario
from src.firebase_init import db

class RegisterWindow:
    def __init__(self, parent, on_close=None):
        self.window = tb.Toplevel(parent)
        self.window.title("Crear nueva cuenta")
        self.window.geometry("400x350")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.on_close = on_close

        frame = tb.Frame(self.window, padding=20)
        frame.pack(expand=True, fill="both")

        tb.Label(frame, text="Nombre de Usuario:").pack(anchor="w")
        self.username_entry = tb.Entry(frame)
        self.username_entry.pack(fill="x", pady=5)

        tb.Label(frame, text="Correo Electrónico:").pack(anchor="w")
        self.email_entry = tb.Entry(frame)
        self.email_entry.pack(fill="x", pady=5)

        tb.Label(frame, text="Contraseña:").pack(anchor="w")
        self.password_entry = tb.Entry(frame, show="*")
        self.password_entry.pack(fill="x", pady=5)

        tb.Label(frame, text="Repetir Contraseña:").pack(anchor="w")
        self.repeat_entry = tb.Entry(frame, show="*")
        self.repeat_entry.pack(fill="x", pady=5)

        tb.Button(frame, text="Crear Cuenta", bootstyle="success", command=self.crear_cuenta).pack(pady=10)
        tb.Button(frame, text="Volver", bootstyle="secondary", command=self.cancelar).pack(pady=5)

    def crear_cuenta(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        repeat = self.repeat_entry.get().strip()

        if not username or not email or not password or not repeat:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        if password != repeat:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        uid = crear_usuario(email, password)
        if uid:
            try:
                db.collection("usuarios").document(uid).set({
                    "nombre": username,
                    "correo": email
                })
                messagebox.showinfo("Éxito", "Cuenta creada correctamente.")
                self.window.destroy()
                if self.on_close:
                    self.on_close()
            except Exception as e:
                messagebox.showerror("Error", f"Fallo al guardar el perfil: {e}")
        else:
            messagebox.showerror("Error", "No se pudo crear el usuario.")

    def cancelar(self):
        self.window.destroy()
        if self.on_close:
            self.on_close()
