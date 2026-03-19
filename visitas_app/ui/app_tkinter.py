import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class App:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Registro de Visitantes")
        self.root.geometry("750x450")
        self.root.configure(bg="#eef2f7")

        # ===== ESTILO =====
        style = ttk.Style()
        style.theme_use("default")

        # ===== FORMULARIO =====
        frame_form = tk.Frame(root, bg="#eef2f7")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Cédula", bg="#eef2f7", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame_form, text="Nombre", bg="#eef2f7", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(frame_form, text="Motivo", bg="#eef2f7", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=10, pady=5)

        self.entry_cedula = tk.Entry(frame_form, width=30)
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_motivo = tk.Entry(frame_form, width=30)

        self.entry_cedula.grid(row=0, column=1, padx=10, pady=5)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)
        self.entry_motivo.grid(row=2, column=1, padx=10, pady=5)

        # ===== BOTONES =====
        frame_btn = tk.Frame(root, bg="#eef2f7")
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Registrar", bg="#4CAF50", fg="white", width=15, command=self.registrar)\
            .grid(row=0, column=0, padx=10)

        tk.Button(frame_btn, text="Eliminar", bg="#f44336", fg="white", width=15, command=self.eliminar)\
            .grid(row=0, column=1, padx=10)

        tk.Button(frame_btn, text="Limpiar", bg="#2196F3", fg="white", width=15, command=self.limpiar)\
            .grid(row=0, column=2, padx=10)

        # ===== TABLA =====
        frame_tabla = tk.Frame(root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(frame_tabla, columns=("Cedula", "Nombre", "Motivo"), show="headings")

        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")

        self.tree.column("Cedula", width=150)
        self.tree.column("Nombre", width=200)
        self.tree.column("Motivo", width=250)

        self.tree.pack(fill="both", expand=True)

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)

        if self.servicio.registrar(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for v in self.servicio.obtener_todos():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def eliminar(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un registro")
            return

        item = self.tree.item(seleccion)
        cedula = item["values"][0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)