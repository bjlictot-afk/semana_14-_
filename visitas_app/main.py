import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import App

if __name__ == "__main__":
    root = tk.Tk()
    servicio = VisitaServicio()  # inyección de dependencia
    app = App(root, servicio)
    root.mainloop()