# funcion yield from
# va a recibir los elementos en forma de tupla en una cantidad
# indeterminada


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento


ciudadesDevueltas = devuelveCiudades(
    "Berlin", "SIdney", "Bruselas", "Tokio", "Cuauhtemoc"
)
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))


# instruccion yield from implementada

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield from elemento


ciudadesDevueltas = devuelveCiudades(
    "Berlin", "SIdney", "Bruselas", "Tokio", "Cuauhtemoc"
)
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
