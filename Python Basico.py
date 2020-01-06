def mensaje():
    print("Estamos aprendiendo Pyhon")
    print("Estamos aprendiendo")


mensaje()
print("Codigo fuera de funcion")
mensaje()
print("Fin de codigo")


def suma(num1, num2):
    resultado = num1 + num2
    return resultado


print(suma(4, 5))
almacenaResulado = suma(5, 7)

miLista = ["Maria", "Pepe", "Jose", "Pablo"]
print(miLista[1:3])
print(miLista)
miLista.append("Hugo")
print(miLista)
miLista.insert(1, "Sandra")
print(miLista)
miLista.remove("Maria")

# tuplas
mitupla = ("Hugo", 133, 45, "Tello")
print(mitupla[0])
lista = list(mitupla)
print(lista)

print(mitupla.count(133))
print(len(mitupla))

#  desenpaquetado de tupllas
# se asginan valores a en el orden que se asignaron
# las variables

nombre, idempleado, sueldo, apellido = mitupla
print(nombre)

# diccionaios
# forma correcta de identar un diccionario
midiccionario = {
    "Alemania": "Berlin", "Australia": "SIdney",
    "Francia": "Paris", 23: "Edad",
    "anillos": {"temporadas": [2002, 2010, 2020]}
}
print(midiccionario["Francia"])
# agregar mas elementos al diccionaios
midiccionario["Italia"] = "Lisboa"
# corregir valor de diccionario
midiccionario["Italia"] = "Roma"
# boorar eleme
del midiccionario["Francia"]
print(midiccionario)
# asignar elemtnos de una tupla  a un midiccionario
mitupla = ["Peru", "Argentina", "Canada"]
midiccionario = {
    mitupla[0]: "Lima", mitupla[1]: "Buenos Aires", mitupla[2]: "Otawa"
}
print(midiccionario)
# print(midiccionario["anillos"])
print(midiccionario.keys)


def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Reprobado"
    return valoracion


print("Programa de evaluacion de notas de alumnos")
# convertir a numero la entrade de teclado
notaalumno = input("Introduce la nota del alumno:")
print(evaluacion(int(notaalumno)))

# condicional else if
print("Control de acceso")
edadUsuario = int(input("Por favor introduce tu edad"))
if edadUsuario < 18:
    print("Puedes pasar")
else:
    print("No puedes pasar")
# estructura elif
print("Estructura elif basica")
acceso = int(input("Por favor ingresa un numero"))
if acceso < 10:
    print("No puedes pasar")
elif acceso < 100:
    print("Acceso no permitido")
else:
    print("Puedes pasar")
