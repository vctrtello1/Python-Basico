from tkinter import Tk, Frame, Label, PhotoImage
root = Tk()
miFrame = Frame(root, width=500, height=600)
miFrame.pack()
miFrame.config(bd=20)
miFrame.config(relief="sunken")
miLabel = Label(miFrame, text="Bienvenido")
# ubicar el texto en una coordenada
miLabel.place(x=10, y=10)
# colocar de manera directa el Label en caso de que no se use
Label(miFrame, text="Segunda etiqueta", fg="red").place(x=10, y=30)
# uso de imagenes
miImagen = PhotoImage(file="jynx.png")
# label con etiqueta
Label(miFrame, image=miImagen, fg="red").place(x=10, y=50)
root.mainloop()
