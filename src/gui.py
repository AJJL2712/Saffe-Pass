import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import os

from password_manager import PasswordManager
from password_generator import generar_contraseña
from src.database_service import guardar_contraseña, leer_contraseñas
from src.firebase_init import db

class PasswordManagerGUI:
    def __init__(self, root, uid):
        self.root = root
        self.uid = uid
        self.root.title("🔐 Gestor de Contraseñas")
        self.root.geometry("700x520")
        self.pm = PasswordManager()

        icon_path = os.path.join("assets", "icono.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.root.option_add("*Font", ("Segoe UI", 11))
        self.tema_actual = "flatly"

        # Panel de bienvenida
        self.panel_usuario = tb.Frame(self.root, padding=10)
        self.panel_usuario.pack(fill="x")
        self.label_bienvenida = tb.Label(self.panel_usuario, text="Bienvenido", font=("Segoe UI", 12, "bold"))
        self.label_bienvenida.pack(side="left")
        self.label_correo = tb.Label(self.panel_usuario, text=self.uid, font=("Segoe UI", 10))
        self.label_correo.pack(side="left", padx=10)
        self.btn_tema = tb.Button(self.panel_usuario, text="🌗 Tema Oscuro", bootstyle="secondary", command=self.toggle_tema)
        self.btn_tema.pack(side="right", padx=5)
        self.btn_logout = tb.Button(self.panel_usuario, text="Cerrar sesión", bootstyle="danger", command=self.root.destroy)
        self.btn_logout.pack(side="right")

        # Cargar nombre desde Firestore
        try:
            doc = db.collection("usuarios").document(self.uid).get()
            if doc.exists:
                datos = doc.to_dict()
                nombre = datos.get("nombre", "Usuario")
                self.label_bienvenida.config(text=f"Bienvenido {nombre}")
        except:
            pass

        frame_datos = tb.LabelFrame(root, text="📜 Nueva Entrada", padding=15)
        frame_datos.pack(fill="x", padx=15, pady=10)

        tb.Label(frame_datos, text="Etiqueta:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_etiqueta = tb.Entry(frame_datos, width=30)
        self.entry_etiqueta.grid(row=0, column=1, padx=5, pady=5)

        self.btn_generar = tb.Button(frame_datos, text="🎲 Generar Contraseña", bootstyle="info", command=self.generar_contraseña)
        self.btn_generar.grid(row=0, column=2, padx=5, pady=5)

        tb.Label(frame_datos, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_contraseña = tb.Entry(frame_datos, width=30, show="*")
        self.entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

        self.btn_mostrar = tb.Checkbutton(frame_datos, text="👁️ Mostrar", bootstyle="secondary", command=self.toggle_password)
        self.btn_mostrar.grid(row=1, column=2, padx=5, pady=5)

        self.btn_guardar = tb.Button(frame_datos, text="💾 Guardar", bootstyle="success", command=self.guardar_contraseña)
        self.btn_guardar.grid(row=2, column=1, columnspan=2, pady=10)

        frame_lista = tb.LabelFrame(root, text="🔐 Contraseñas Guardadas", padding=15)
        frame_lista.pack(fill="both", expand=True, padx=15, pady=10)

        self.listbox_etiquetas = tk.Listbox(frame_lista, height=10, width=40, font=("Segoe UI", 10))
        self.listbox_etiquetas.pack(side="left", fill="both", expand=True, padx=(0, 10))

        botones_frame = tb.Frame(frame_lista)
        botones_frame.pack(side="right", fill="y")

        self.btn_eliminar = tb.Button(botones_frame, text="🗑️ Eliminar", bootstyle="danger", command=self.eliminar_contraseña)
        self.btn_eliminar.pack(fill="x", pady=5)

        self.btn_mostrar_contraseña = tb.Button(botones_frame, text="👁️ Ver", bootstyle="info", command=self.mostrar_contraseña_manual)
        self.btn_mostrar_contraseña.pack(fill="x", pady=5)

        self.status_label = tb.Label(root, text="Bienvenido al gestor de contraseñas", anchor="w", relief="sunken")
        self.status_label.pack(fill="x", padx=15, pady=(0, 10))

        self.cargar_etiquetas()

    def toggle_password(self):
        if self.entry_contraseña.cget("show") == "":
            self.entry_contraseña.config(show="*")
        else:
            self.entry_contraseña.config(show="")

    def toggle_tema(self):
        nuevo = "darkly" if self.tema_actual == "flatly" else "flatly"
        self.root.style.theme_use(nuevo)
        self.tema_actual = nuevo
        self.btn_tema.config(text="🌞 Tema Claro" if nuevo == "darkly" else "🌗 Tema Oscuro")

    def generar_contraseña(self):
        contraseña = generar_contraseña()
        self.entry_contraseña.delete(0, "end")
        self.entry_contraseña.insert(0, contraseña)
        self.status_label.config(text="Contraseña generada ✅")

    def guardar_contraseña(self):
        etiqueta = self.entry_etiqueta.get().strip()
        contraseña = self.entry_contraseña.get().strip()
        if not etiqueta or not contraseña:
            messagebox.showerror("Error", "Por favor, llena todos los campos.")
            return
        guardar_contraseña(self.uid, etiqueta, self.uid, contraseña)
        self.entry_etiqueta.delete(0, "end")
        self.entry_contraseña.delete(0, "end")
        self.status_label.config(text=f"Contraseña guardada para '{etiqueta}' ✅")
        self.cargar_etiquetas()

    def cargar_etiquetas(self):
        self.listbox_etiquetas.delete(0, "end")
        contraseñas = leer_contraseñas(self.uid)
        for etiqueta in contraseñas:
            self.listbox_etiquetas.insert("end", etiqueta)

    def mostrar_contraseña_manual(self):
        seleccion = self.listbox_etiquetas.curselection()
        if seleccion:
            etiqueta = self.listbox_etiquetas.get(seleccion)
            contraseñas = leer_contraseñas(self.uid)
            datos = contraseñas.get(etiqueta)
            if datos:
                contraseña = datos.get("contrasena")
                self.mostrar_contraseña_modal(etiqueta, contraseña)

    def mostrar_contraseña_modal(self, etiqueta, contraseña):
        ventana = tb.Toplevel(self.root)
        ventana.title("🔐 Ver Contraseña")
        ventana.geometry("400x200")
        ventana.resizable(False, False)
        ventana.grab_set()

        contenedor = tb.Frame(ventana, padding=20)
        contenedor.pack(expand=True, fill="both")

        tb.Label(contenedor, text="Etiqueta", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        tb.Label(contenedor, text=etiqueta, font=("Segoe UI", 11)).pack(anchor="w", pady=(0, 10))

        tb.Label(contenedor, text="Contraseña", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        frame_pw = tb.Frame(contenedor)
        frame_pw.pack(fill="x", pady=5)

        entry_pw = tb.Entry(frame_pw, font=("Segoe UI", 11), width=30)
        entry_pw.insert(0, contraseña)
        entry_pw.config(state="readonly")
        entry_pw.pack(side="left", fill="x", expand=True, padx=(0, 5))

        def copiar():
            self.root.clipboard_clear()
            self.root.clipboard_append(contraseña)
            self.status_label.config(text=f"Contraseña copiada al portapapeles 📋")

        tb.Button(frame_pw, text="📋", width=5, bootstyle="info", command=copiar).pack(side="right")
        tb.Button(contenedor, text="Cerrar", bootstyle="secondary", command=ventana.destroy).pack(pady=15)

    def eliminar_contraseña(self):
        seleccion = self.listbox_etiquetas.curselection()
        if seleccion:
            etiqueta = self.listbox_etiquetas.get(seleccion)
            if messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar '{etiqueta}'?"):
                contraseñas = leer_contraseñas(self.uid)
                doc_ref = db.collection('usuarios').document(self.uid).collection('passwords').document(etiqueta)
                doc_ref.delete()
                self.cargar_etiquetas()
                self.status_label.config(text=f"'{etiqueta}' ha sido eliminada 🗑️")
