import sqlite3
miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()
miCursor.execute(
    "Create table Productos (Id Integer Primary Key Autoincrement,"
    "NombreArticulo Varchar(50) Unique, Precio Integer, Seccion Varchar(50))"
)
variosProductos = [
    ("Camiseta", 10, "Deportes"), ("Jarron", 100, "Ceramica"),
    ("Rifle", 2600, "Armas")
    ]
miCursor.executemany(
    # se usa Null para que tome como vacio el primer campo que es el id
    # el cual se autoincrementa y es llave primaria
    "Insert into Productos values (NULL,?,?,?)", variosProductos)
miConexion.commit()
miConexion.close()
