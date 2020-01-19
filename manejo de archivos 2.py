from io import open
archivoTexto = open("archivo2.txt", "r")
print(archivoTexto.read())
archivoTexto.seek(2)
print(archivoTexto.read())
archivoTexto.close()
