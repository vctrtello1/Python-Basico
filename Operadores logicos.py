# condficional if
print("Programa de Becas")
distancia_escuela = int(input("Introduce la distancia de la escuela en Km: "))
print(distancia_escuela)
numero_hermanos = int(input("Introduce el numero de hermanos: "))
print(numero_hermanos)
salario_familiar = int(input("Introduce el salario familiar: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or \
 salario_familiar <= 20000:
    print("Tienes derecho a una beca")
else:
    print("No tienes derecho a una beca")

# operador in
print("Asignaturas optativas")
print("Informatica grafica, Pruebas de software, Usabilidad y accesibilidad")
asignatura = input("Escribe la asignatura que vas a cursar: ")
# Python es sensible a las mayusculas y minusculas
# podemos usar lower y upper
if asignatura in (
    "Informatica grafica", "Pruebas de software",
    "Usabilidad y accesibilidad"
):
    print("Asignatura asignada: " + asignatura)
else:
    print("La asignatura solicitada no existe")
