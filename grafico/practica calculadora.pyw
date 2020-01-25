from tkinter import Tk, Frame, Entry, Button, StringVar
root = Tk()
miFrame = Frame(root)
miFrame.pack()
# variable para numeros en pantalla
numeroPantalla = StringVar()
# pantalla
# asociar la variable de entrada a la pantalla
pantalla = Entry(miFrame, textvariable=numeroPantalla)
# columnspan es para que ocupe 4 columanas en el grid
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
# ajustamos el texto a la derecha con la funcion justify
pantalla.config(background="black", fg="green", justify="right")

# ingresos de texto a la pantalla


# hace una concatenacion de lo que estaba anteriormente y le agrega el
# numero 4 en este caso
def numeroPulsado(numero):
    numeroPantalla.set(numeroPantalla.get() + numero)


# botones
boton7 = Button(
    miFrame, text="7", width=3, padx=10, pady=10, command=numeroPulsado("7")
    ).grid(row=2, column=1)
boton8 = Button(
    miFrame, text="8", width=3, padx=10, pady=10, command=numeroPulsado("8")
    ).grid(row=2, column=2)
boton9 = Button(
    miFrame, text="9", width=3, padx=10, pady=10, command=numeroPulsado("9")
    ).grid(row=2, column=3)
botonMultiplicar = Button(
    miFrame, text="X", width=3, padx=10, pady=10, command=numeroPulsado("X")
    ).grid(row=2, column=4)
boton4 = Button(
    miFrame, text="4", width=3, padx=10, pady=10, command=numeroPulsado("4")
    ).grid(row=3, column=1)
boton5 = Button(
    miFrame, text="5", width=3, padx=10, pady=10, command=numeroPulsado("5")
    ).grid(row=3, column=2)
boton6 = Button(
    miFrame, text="6", width=3, padx=10, pady=10, command=numeroPulsado("6")
    ).grid(row=3, column=3)
botonDividir = Button(
    miFrame, text="/", width=3, padx=10, pady=10, command=numeroPulsado("/")
    ).grid(row=3, column=4)
boton1 = Button(
    miFrame, text="1", width=3, padx=10, pady=10, command=numeroPulsado("1")
    ).grid(row=4, column=1)
boton2 = Button(
    miFrame, text="2", width=3, padx=10, pady=10, command=numeroPulsado("2")
    ).grid(row=4, column=2)
boton3 = Button(
    miFrame, text="3", width=3, padx=10, pady=10, command=numeroPulsado("3")
    ).grid(row=4, column=3)
botonSumar = Button(
    miFrame, text="+", width=3, padx=10, pady=10, command=numeroPulsado("+")
    ).grid(row=4, column=4)
boton0 = Button(
    miFrame, text="0", width=3, padx=10, pady=10, command=numeroPulsado("0")
    ).grid(row=5, column=1)
botonPunto = Button(
    miFrame, text=".", width=3, padx=10, pady=10, command=numeroPulsado(".")
    ).grid(row=5, column=2)
botonPotencia = Button(
    miFrame, text="^", width=3, padx=10, pady=10, command=numeroPulsado("^")
    ).grid(row=5, column=3)
botonResar = Button(
    miFrame, text="-", width=3, padx=10, pady=10, command=numeroPulsado("-")
    ).grid(row=5, column=4)

root.mainloop()
