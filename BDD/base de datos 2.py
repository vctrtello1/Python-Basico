import sqlite3
miConexion = sqlite3.connect("PrimeraBase")
# instanciar el cursor
miCursor = miConexion.cursor()
# se usa una tupla para guardar los registros
variosProductos = [
    ("Camiseta", 10, "Deportes"), ("Jarron", 100, "Ceramica"),
    ("Rifle", 2600, "Armas")
    ]
# de esta manera mandamos la informacion a la tabla
# la cual estamos enviando la tupla que creamos arriba
miCursor.executemany("Insert into Productos values (?,?,?)", variosProductos)
miConexion.commit()
miConexion.close()
