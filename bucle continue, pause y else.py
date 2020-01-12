# operaciones basicas
for letra in "Python":
    # ignorar la letra h para continuar con la operacion
    if letra == "h":
        continue
    print("Estas viendo la letra: " + letra)
nombre = "Pildoras Informaticas"
contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1
print("La longitud de la cadena sin espacio es: " + str(contador))

# instruccion pass


class MiClass:
    pass  # para implementar mas tarde, se ejecuta cuando el bucle se haya
    # ejecutado


# instuccion else
email = input("Introduce tu email por favor: ")
for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False
print(arroba)
