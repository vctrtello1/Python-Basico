# Ciclos de control
# bucle for
for i in [1, 2, 3]:
    print("Hola: " + str(i))

for j in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(j)
# uso de la instuccion end, para fin de linea
for k in [1, 2, 3]:
    print("Hola ", end=" ")
# recorrer una cadena
print("\n \n")  # salto de linea
for k in "Hola":
    print(k)

# analizar la cadena para saber si existe un elemento en concreto
# en el siguiente caso se buscara un arroba para saber si se
# trata de un correo electronico
for iter in "victorhugotello@hotmail.com":
    if iter == "@":
        email = True

if email:
    print("Se trata de una direccion de correo")
else:
    print("No se trata de una direccion de correo")

# validacion de un correo ingresado de manera manual
mi_email = input("Introduce tu email: ")
for ix in mi_email:
    if ix == "@":
        email_valido = True
    else:
        email_valido = False
if email_valido:
    print("El email esta correctamente validado")

# tipo Range
for im in range(8):
    print("Hola")
    # concatencacion
    print(f"nivel {im}")
# tipo range con salto especifico
for im in range(8, 50, 3):
    print(f"nivelx {im}")
# ciclo while
