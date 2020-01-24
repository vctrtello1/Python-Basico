from tkinter import Tk, Frame, Entry, Label, Text, Scrollbar
root = Tk()
miFrame = Frame(root, width=500, height=600)
miFrame.pack()
miFrame.config(bd=20)
miFrame.config(relief="sunken")
# cuadroTexto = Entry(miFrame).place(x=10, y=20)
# metodo grid para realizar tablas
# se usa la propiedad sticky la cual va con puntos cardinales y
# tambien se pueden usar punto intermedios como suresre
cuadroTexto = Entry(miFrame).grid(
    row=0, column=1, pady=10, padx=10
    )
nombreLabel = Label(miFrame, text="Nombre: ").grid(
    row=0, column=0, sticky="e", pady=10, padx=10
    )
cuadroTextoApellido = Entry(miFrame).grid(
    row=1, column=1, sticky="e", pady=10, padx=10
    )
apellidoLabel = Label(miFrame, text="Apellido: ").grid(
    row=1, column=0, sticky="e", pady=10, padx=10
    )
cuadroTextoDireccion = Entry(miFrame).grid(
    row=2, column=1, sticky="e", pady=10, padx=10
    )
direccionLabel = Label(miFrame, text="Direccion: ").grid(
    row=2, column=0, sticky="e", pady=10, padx=10
    )
cuadroTextoPassword = Entry(miFrame).grid(
    row=3, column=1, pady=10, padx=10
    )
passwordLabel = Label(miFrame, text="Password: ").grid(
    row=3, column=0, sticky="e", pady=10, padx=10
    )
comentariosLabel = Label(miFrame, text="Comentarios: ").grid(
    row=4, column=0, sticky="e", pady=10, padx=10
    )
textoComentario = Text(miFrame, width=25, height=6)
# se separa el grid para que poder instanciar los construimos
# componentes
textoComentario.grid(
    row=4, column=1, sticky="e", pady=10, padx=10
    )
# forma en la construimos y asignamos el scrollbar a la caja de texto
# a el frame
scrollTextoComentarios = Scrollbar(miFrame, command=textoComentario.yview)
scrollTextoComentarios.grid(row=4, column=2)
root.mainloop()
