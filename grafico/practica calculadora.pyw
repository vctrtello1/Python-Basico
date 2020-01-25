from tkinter import Tk, Frame, Entry, Button, StringVar
root = Tk()
miFrame = Frame(root)
miFrame.pack()
# variable para asignarr la operacion
operacion = ""
# variable global para resultado
resultado = 0
# variable para numeros en pantalla
numeroPantalla = StringVar()
# pantalla
# asociar la variable de entrada a la pantalla
pantalla = Entry(miFrame, textvariable=numeroPantalla)
# columnspan es para que ocupe 4 columanas en el grid
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
# ajustamos el texto a la derecha con la funcion justify
pantalla.config(background="black", fg="white", justify="right")

# ingresos de texto a la pantalla


# hace una concatenacion de lo que estaba anteriormente y le agrega el
def numeroPulsado(numero):
    # revisa que si es una nueva operacion
    global operacion
    if operacion != "":
        numeroPantalla.set(numero)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + numero)


def suma(numero):
    # se almacena dentro de la variable global suma
    global operacion
    global resultado
    resultado += int(numero)
    operacion = "suma"
    numeroPantalla.set(resultado)


def resta(numero):
    # se almacena dentro de la variable global suma
    global operacion
    global resultado
    resultado -= int(numero)
    operacion = "resta"
    numeroPantalla.set(resultado)


def division(numero):
    # se almacena dentro de la variable global suma
    global operacion
    global resultado
    resultado /= int(numero)
    operacion = "division"
    numeroPantalla.set(resultado)


def multiplicacion(numero):
    # se almacena dentro de la variable global suma
    global operacion
    global resultado
    resultado += int(numero)
    operacion = "multiplicacion"
    numeroPantalla.set(resultado)


def resultadoOperacion():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0


# botones
# se usa la funcion lambda para que sea una funcion anonima, de otra manera
# la funcion command ejecuta el las funciones
boton7 = Button(
    miFrame, text="7", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("7")
    ).grid(row=2, column=1)
boton8 = Button(
    miFrame, text="8", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("8")
    ).grid(row=2, column=2)
boton9 = Button(
    miFrame, text="9", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("9")
    ).grid(row=2, column=3)
botonMultiplicar = Button(
    miFrame, text="X", width=3, padx=10, pady=10,
    command=lambda: multiplicacion(numeroPantalla.get())
    ).grid(row=2, column=4)
boton4 = Button(
    miFrame, text="4", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("4")
    ).grid(row=3, column=1)
boton5 = Button(
    miFrame, text="5", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("5")
    ).grid(row=3, column=2)
boton6 = Button(
    miFrame, text="6", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("6")
    ).grid(row=3, column=3)
botonDividir = Button(
    miFrame, text="/", width=3, padx=10, pady=10,
    command=lambda: division(numeroPantalla.get())
    ).grid(row=3, column=4)
boton1 = Button(
    miFrame, text="1", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("1")
    ).grid(row=4, column=1)
boton2 = Button(
    miFrame, text="2", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("2")
    ).grid(row=4, column=2)
boton3 = Button(
    miFrame, text="3", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("3")
    ).grid(row=4, column=3)
botonSumar = Button(
    miFrame, text="+", width=3, padx=10, pady=10,
    command=lambda: suma(numeroPantalla.get())
    ).grid(row=4, column=4)
boton0 = Button(
    miFrame, text="0", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado("0")
    ).grid(row=5, column=1)
botonPunto = Button(
    miFrame, text=".", width=3, padx=10, pady=10,
    command=lambda: numeroPulsado(".")
    ).grid(row=5, column=2)
botonIgual = Button(
    miFrame, text="=", width=3, padx=10, pady=10,
    command=lambda: resultadoOperacion()
    ).grid(row=5, column=3)
botonRestar = Button(
    miFrame, text="-", width=3, padx=10, pady=10,
    command=lambda: resta(numeroPantalla.get())
    ).grid(row=5, column=4)

root.mainloop()
