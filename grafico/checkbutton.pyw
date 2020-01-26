from tkinter import Tk, Frame, Checkbutton, PhotoImage, Label, IntVar
root = Tk()
root.title("Ejemplo de Radiobutton")
playa = IntVar()
montania = IntVar()
rural = IntVar()


def opcionesViaje():
    opcionEscogida = ""
    if(playa.get() == 1):
        opcionEscogida += " playa"
    if(montania.get() == 1):
        opcionEscogida += " montaña"
    if(rural.get() == 1):
        opcionEscogida += " rural"
    textoFinal.config(text=opcionEscogida)


miFrame = Frame(root, width=500, height=600)
miFrame.pack()

miFrame.config(bd=20)
foto = PhotoImage(file="avion.png")
Label(miFrame, image=foto).pack()
Label(miFrame, text="Elige destino").pack()
Checkbutton(
    # se usa la funcion onvalue para saber que esta seleccionado y
    # la funcion offvalue para que esta sin seleccionar
    miFrame, text="Playa", variable=playa, onvalue=1, offvalue=0,
    command=lambda: opcionesViaje()
).pack()
Checkbutton(
    miFrame, text="Montaña", variable=montania, onvalue=1, offvalue=0,
    command=lambda: opcionesViaje()
    ).pack()
Checkbutton(
    miFrame, text="Rural", variable=rural, onvalue=1, offvalue=0,
    command=lambda: opcionesViaje()
    ).pack()
textoFinal = Label(miFrame)
textoFinal.pack()
root.mainloop()
