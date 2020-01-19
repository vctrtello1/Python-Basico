import pickle
# leer archivo binario
fichero = open("lista", "rb")
listaBinario = pickle.load(fichero)
print(listaBinario)
