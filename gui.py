import tkinter as tk
from tkinter import ttk, messagebox
from password_manager import PasswordManager
from password_generator import generar_contraseña

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Contraseñas")
        self.pm = PasswordManager()

        # Usar estilos de ttk
        style = ttk.Style()
        style.theme_use("clam")  # Cambiar a un estilo moderno

        # Etiqueta para nombre/servicio
        self.label_etiqueta = ttk.Label(root, text="Etiqueta:")
        self.label_etiqueta.grid(row=0, column=0, padx=5, pady=5)

        self.entry_etiqueta = ttk.Entry(root, width=30)
        self.entry_etiqueta.grid(row=0, column=1, padx=5, pady=5)

        # Botón para generar contraseña
        self.btn_generar = ttk.Button(root, text="Generar Contraseña", command=self.generar_contraseña)
        self.btn_generar.grid(row=0, column=2, padx=5, pady=5)

        # Entrada para contraseña generada
        self.entry_contraseña = ttk.Entry(root, width=30)
        self.entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

        # Botón para guardar contraseña
        self.btn_guardar = ttk.Button(root, text="Guardar", command=self.guardar_contraseña)
        self.btn_guardar.grid(row=1, column=2, padx=5, pady=5)

        # Lista de etiquetas
        self.label_lista = ttk.Label(root, text="Etiquetas guardadas:")
        self.label_lista.grid(row=2, column=0, padx=5, pady=5)

        self.listbox_etiquetas = tk.Listbox(root, height=10, width=30)
        self.listbox_etiquetas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.listbox_etiquetas.bind("<<ListboxSelect>>", self.mostrar_contraseña)

        # Botón para eliminar
        self.btn_eliminar = ttk.Button(root, text="Eliminar", command=self.eliminar_contraseña)
        self.btn_eliminar.grid(row=3, column=2, padx=5, pady=5)

        # Inicializar lista de etiquetas
        self.cargar_etiquetas()

    def generar_contraseña(self):
        contraseña = generar_contraseña()
        self.entry_contraseña.delete(0, tk.END)
        self.entry_contraseña.insert(0, contraseña)

    def guardar_contraseña(self):
        etiqueta = self.entry_etiqueta.get().strip()
        contraseña = self.entry_contraseña.get().strip()
        if not etiqueta or not contraseña:
            messagebox.showerror("Error", "Por favor, llena todos los campos.")
            return
        self.pm.agregar_password(etiqueta, contraseña)
        self.cargar_etiquetas()
        self.entry_etiqueta.delete(0, tk.END)
        self.entry_contraseña.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Contraseña guardada para '{etiqueta}'.")

    def cargar_etiquetas(self):
        self.listbox_etiquetas.delete(0, tk.END)
        for etiqueta in self.pm.listar_etiquetas():
            self.listbox_etiquetas.insert(tk.END, etiqueta)

    def mostrar_contraseña(self, event):
        seleccion = self.listbox_etiquetas.curselection()
        if seleccion:
            etiqueta = self.listbox_etiquetas.get(seleccion)
            contraseña = self.pm.obtener_password(etiqueta)
            messagebox.showinfo(f"Contraseña para '{etiqueta}'", f"{contraseña}")

    def eliminar_contraseña(self):
        seleccion = self.listbox_etiquetas.curselection()
        if seleccion:
            etiqueta = self.listbox_etiquetas.get(seleccion)
            if messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar '{etiqueta}'?"):
                self.pm.eliminar_password(etiqueta)
                self.cargar_etiquetas()
                messagebox.showinfo("Éxito", f"'{etiqueta}' ha sido eliminada.")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
