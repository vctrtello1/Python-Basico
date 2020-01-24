from tkinter import Tk, Frame
# se cambia la extension a .pyw para ventana
raiz = Tk()
raiz.title("Ventana de prueba")
raiz.resizable(False, False)
raiz.iconbitmap("bateria.ico")
# raiz.geometry("640x350")
# frame para trabar
miFrame = Frame()
miFrame.pack()
miFrame.config(bd=20)
miFrame.config(relief="sunken")
miFrame.config(width="640", height="350")
# debe estar al final de la operacion
raiz.mainloop()
