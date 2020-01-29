from tkinter import Tk, Menu, messagebox
import sqlite3
root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300)
bddMenu = Menu(barraMenu, tearoff=0)
bddMenu.add_command(label="Conectar")
bddMenu.add_command(label="Salir")
root.mainloop()
