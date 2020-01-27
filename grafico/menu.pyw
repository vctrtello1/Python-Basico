from tkinter import Tk, Frame, Menu, messagebox
root = Tk()


# ventanas emergentes
def informacionAdicional():
    messagebox.showinfo("Acerca de", "Programe de practica")


def informacionDeLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia Gnu")


def salidaDeAplicacion():
    valor = messagebox.askquestion("Salir", "Deseas salir de la apliacion?")
    if valor == "yes":
        # finalizar programa
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        "Reintentar", "No es posible cerrar documento"
    )
    if valor is False:
        root.destroy()


miFrame = Frame(root, width=500, height=600)
miFrame.pack()
miFrame.config(bd=20)
barraMenu = Menu(root)
root.config(menu=barraMenu)
# se usa la propiedad tearoff en 0 para quitar la sangria
# en el menu
archivoMenu = Menu(barraMenu, tearoff=0)
# agregar elementos al menu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir archivo")
archivoMenu.add_command(label="Abrir carpeta")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Todo")
# agregar separador
archivoMenu.add_separator()
archivoMenu.add_command(
    label="Cerrar", command=lambda: cerrarDocumento()
    )
archivoMenu.add_command(
    label="Salir", command=lambda: salidaDeAplicacion()
    )
archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(
    label="Licencia", command=lambda: informacionDeLicencia()
    )
archivoAyuda.add_command(
    label="Acerca de", command=lambda: informacionAdicional()
    )
# agregar elementos a la barra de Menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
root.mainloop()
