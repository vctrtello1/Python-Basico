import sqlite3
miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()
# actualidar
miCursor.execute(
    "Update Productos set Precio = 11 where NombreArticulo ='Camiseta'"
    )
miConexion.commit()
miConexion.close()
