from tkinter import Tk, Menu, Frame, Entry, Text, Scrollbar
# import sqlite3
root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
bddMenu = Menu(barraMenu, tearoff=0)
bddMenu.add_command(label="Conectar")
bddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="crear")
crudMenu.add_command(label="leer")
crudMenu.add_command(label="actualizar")
crudMenu.add_command(label="borrar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BDD", menu=bddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# comienzo de campos
miFrame = Frame(root)
miFrame.pack()
cuadroId = Entry(miFrame)
cuadroId.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre = Entry(miFrame).grid(row=1, column=1, padx=10, pady=10)
cuadroPass = Entry(miFrame).grid(row=2, column=1, padx=10, pady=10)
cuadroApellido = Entry(miFrame).grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion = Entry(miFrame).grid(row=4, column=1, padx=10, pady=10)
textoComentario = Text(
    miFrame, width=16, height=5
    )
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2)

root.mainloop()
