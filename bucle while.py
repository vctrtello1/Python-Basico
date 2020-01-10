import math
# bucle while
i = 1
while i <= 10:
    print("Hola")
    print("Ejecucion" + str(i))
    i = i + 1
print("Fin de Ejecucion")

# ciclo while con entrada indefinida
edad = int(input("Introduce tu edad por favor: "))
while edad < 0 or edad > 100:
    print("Introduce una edad positiva por favor")
    edad = int(input("Introduce tu edad por favor: "))
print("Gracias por colaborar")
print("Tu edad es:" + str(edad))

# programa de calculo de raiz cuadrada
print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero positivo"))
intentos = 0
while numero > 0:
    print("No se puede encontrar la raiz de un numero negativo")
    if intentos == 2:
        print("Has terminado con tu numero de intentos")
        break
        numero = int(input("Introduce un numero positivo"))
        if numero < 0:
            intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))
