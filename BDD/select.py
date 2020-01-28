import sqlite3
miConexion = sqlite3.connect("PrimeraBase")
# instanciar el cursor
miCursor = miConexion.cursor()
miCursor.execute("Select * from Productos")
# almacenamos nuestra respuesta
variosProductos = miCursor.fetchall()
print(variosProductos)
miConexion.commit()
miConexion.close()
