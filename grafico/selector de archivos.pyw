from tkinter import Tk, filedialog, Button
root = Tk()


def abrirFichero():
    fichero = filedialog.askopenfilename(
        title="Abrir", initialdir="C:",
        filetypes=(
            ("Archivos de imagen", "*.jpg"), ("Archivos de imagen", "*.png"),
            ("Todos los archivos", "*.*")
        )
    )
    print(fichero)


Button(
    root, text="Abrir Fichero", command=lambda: abrirFichero()
    ).pack()
root.mainloop()
