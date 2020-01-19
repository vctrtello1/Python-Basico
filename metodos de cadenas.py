nombreUsuario = input("Introduce el nombre de usuario: ")
# pasar a mayusulas
print("El nombre de usuario es: ", nombreUsuario.upper())
# pasar a minusculass
print("El nombre de usuario es: ", nombreUsuario.lower())
# primera letra en mayusula
print("El nombre de usuario es: ", nombreUsuario.capitalize())
# comprobar si es numero
if nombreUsuario.isdigit():
    print("Es numero")
else:
    print("No es numero")
