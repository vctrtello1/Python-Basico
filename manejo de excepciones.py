def cuadrado(x):
    y = x ** 2
    return y


result = cuadrado(3)
print(result)


# manejo de excepciones


def cuadradoExcepcion(numero):
    try:
        return numero / 2
    except ValueError as ex:
        print("Excepcion de tipo Value:")
        print(ex)
    except TypeError as ex:
        print("Excepcion de tipo Type:")
        print(ex)


print(cuadradoExcepcion("12"))
print("La operacion continua")
print(cuadradoExcepcion(12))


# finally
def divide():
    try:
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
        return numero1/numero2
    except ValueError:
        print("Error de datos")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Operacion finalizada")
# finally se ejecuta si o si, puede ser util para cerrar
# conexion de bases de datos o funciones que se necesitan
# ejecuar


print(divide())
