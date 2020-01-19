class Humano():  # Creamos la clase Humano
    def __init__(self, edad, nombre):  # Definimos el atributo edad y nombre
        self.edad = edad
        self.nombre = nombre


Persona1 = Humano(31, "Pedro")  # Instancia
print(Persona1.edad)
