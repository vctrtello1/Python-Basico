import pickle
listaNombres = ["le Bagre", "Marruco"]
# escritura binario
ficheroBinario = open("lista", "wb")
pickle.dump(listaNombres, ficheroBinario)
ficheroBinario.close()
del(ficheroBinario)
