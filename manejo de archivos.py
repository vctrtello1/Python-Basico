from io import open
archivoTexto = open("archivo.txt", "w")
frase = "Buen dia"
archivoTexto.write(frase)
archivoTexto.close()
# podemos usar el metodo readlines() para pasar el archivo a una lista
