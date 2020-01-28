import sqlite3
miConexion = sqlite3.connect("PrimeraBase")
# instanciar el cursor
miCursor = miConexion.cursor()
miCursor.execute(
    # sentencia SQL para generar tabla
    # "Create table Productos(NombreArticulo Varchar(50),"\
    # "Precio Integer, Seccion Varchar(20))"
    "Insert into Productos values('Balon',15 ,'Deportes')"
)
# se realiza la confirmacion del la insercion
# con el metodo commit
miConexion.commit()
miConexion.close()
