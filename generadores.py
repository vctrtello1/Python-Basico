# manejo de generadores
# funcion tradcional


def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num += 1
        return miLista
# generador con la misma operacion que la funcion anterior


def generaParesGenerador(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1


devuelvePares = generaParesGenerador(10)
print(next(devuelvePares))
# entra en un estado de suspencion despues de ejeuctarse el generador
print("Aqui podria ir mas codigo")
print(next(devuelvePares))
print("Aqui podria ir mas codigo")
print(next(devuelvePares))


# instuccion yield from
