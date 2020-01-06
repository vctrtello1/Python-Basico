print("Verificacion de acceso")
nota_alumno = int(input("Introduce tu nota por favor: "))
if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno < 6:
    print("Suficiente")
elif nota_alumno < 7:
    print("Aceptable")
elif nota_alumno < 8:
    print("Bien")
elif nota_alumno < 9:
    print("Muy bien")
else:
    print("Sobresaliente")
# condicionles Python
# concatencacion de operadores condicionales
edad = -7
if 0 < edad < 100:
    print("La edad es correcta")
else:
    print("La edad es incorrecta")
# programa para evalucar salarios
salario_presidente = int(input("Introduce el salario del presiente:"))
print("El salario del presidente es:" + str(salario_presidente))

salario_director = int(input("Introduce el salario del director:"))
print("El salario del director es:" + str(salario_director))

salario_jefe_de_area = int(input("Introduce el salario del jefe de area:"))
print("El salario del presidente es:" + str(salario_jefe_de_area))

salario_administrativo = int(input("Introduce el salario del administrativo:"))
print("El salario del administrativo es:" + str(salario_administrativo))


# salto de linea en if
if salario_administrativo < salario_jefe_de_area < salario_director\
 < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo esta mal en la empresa")
