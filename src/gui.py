import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from password_manager import PasswordManager
from password_generator import generar_contraseña
import os

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Gestor de Contraseñas")
        self.root.geometry("700x520")
        self.pm = PasswordManager()

        # Establecer icono si existe
        icon_path = os.path.join("assets", "icono.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.root.option_add("*Font", ("Segoe UI", 11))
        self.tema_actual = "flatly"

        top_frame = tb.Frame(root, padding=10)
        top_frame.pack(fill="x")

        self.btn_tema = tb.Button(top_frame, text="🌗 Tema Oscuro", bootstyle="secondary", command=self.toggle_tema)
        self.btn_tema.pack(side="right", padx=5)

        self.btn_limpiar = tb.Button(top_frame, text="🧹 Limpiar Campos", bootstyle="warning", command=self.limpiar_campos)
        self.btn_limpiar.pack(side="right", padx=5)

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

    def limpiar_campos(self):
        self.entry_etiqueta.delete(0, "end")
        self.entry_contraseña.delete(0, "end")
        self.status_label.config(text="Campos limpiados 🧹")

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
        self.pm.agregar_password(etiqueta, contraseña)
        self.cargar_etiquetas()
        self.entry_etiqueta.delete(0, "end")
        self.entry_contraseña.delete(0, "end")
        self.status_label.config(text=f"Contraseña guardada para '{etiqueta}' ✅")

    def cargar_etiquetas(self):
        self.listbox_etiquetas.delete(0, "end")
        for etiqueta in self.pm.listar_etiquetas():
            self.listbox_etiquetas.insert("end", etiqueta)

    def mostrar_contraseña_manual(self):
        seleccion = self.listbox_etiquetas.curselection()
        if seleccion:
            etiqueta = self.listbox_etiquetas.get(seleccion)
            contraseña = self.pm.obtener_password(etiqueta)
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
                self.pm.eliminar_password(etiqueta)
                self.cargar_etiquetas()
                self.status_label.config(text=f"'{etiqueta}' ha sido eliminada 🖑")

if __name__ == "__main__":
    app = PasswordManagerGUI(tb.Window(themename="flatly"))
    app.root.mainloop()
