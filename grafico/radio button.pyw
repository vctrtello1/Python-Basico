from tkinter import Tk, Frame, Radiobutton, IntVar, Label
root = Tk()

opcion = IntVar()


def imprimirGenero():
    # mostrar en una etiqueta el genero de la persona
    if opcion.get() == 1:
        etiquetaGenero.config(text="Masculino")
    else:
        etiquetaGenero.config(text="Femenino")


miFrame = Frame(root, width=500, height=600)
miFrame.pack()
miFrame.config(bd=20)
Label(miFrame, text="Genero").pack()
miFrame.config(relief="sunken")
Radiobutton(
    miFrame, text="Masculino", variable=opcion, value=1,
    command=lambda: imprimirGenero()
    ).pack()
Radiobutton(
    miFrame, text="Femenino", variable=opcion, value=2,
    command=lambda: imprimirGenero()
    ).pack()
etiquetaGenero = Label(miFrame)
etiquetaGenero.pack()
root.mainloop()
