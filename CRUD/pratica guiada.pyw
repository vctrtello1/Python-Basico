from tkinter import Tk, Menu, Frame, Entry, Text, Scrollbar, Label, Button
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
# es necesario separar el grid en otra linea para poder realizar
# la operacion
textoComentario = Text(
    miFrame, width=16, height=5
    )
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

idLabel = Label(miFrame, text="Id:").grid(
    row=0, column=0, sticky="e", padx=10, pady=10
    )
nombreLabel = Label(miFrame, text="Nombre:").grid(
    row=1, column=0, sticky="e", padx=10, pady=10
    )
passLabel = Label(miFrame, text="Password:").grid(
    row=2, column=0, sticky="e", padx=10, pady=10
    )
apellidoLabel = Label(miFrame, text="Apellido:").grid(
    row=3, column=0, sticky="e", padx=10, pady=10
    )
direccionLabel = Label(miFrame, text="Direccion:").grid(
    row=4, column=0, sticky="e", padx=10, pady=10
    )
comentariosLabel = Label(miFrame, text="Comentarios:").grid(
    row=5, column=0, sticky="e", padx=10, pady=10
    )
# frame para los botones
miFrameBotones = Frame(root)
miFrameBotones.pack()
botonCrear = Button(miFrameBotones, text="Create").grid(
    row=1, column=0, sticky="e", padx=10, pady=10
    )
botonLeer = Button(miFrameBotones, text="Read").grid(
    row=1, column=1, sticky="e", padx=10, pady=10
    )
botonActualizar = Button(miFrameBotones, text="Update").grid(
    row=1, column=2, sticky="e", padx=10, pady=10
    )
botonBorrar = Button(miFrameBotones, text="Delete").grid(
    row=1, column=3, sticky="e", padx=10, pady=10
    )
root.mainloop()
