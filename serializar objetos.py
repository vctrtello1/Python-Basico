import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelar = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelar(self):
        self.acelar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print(
            "Marca: ", self.marca, ", Modelo: ", self.modelo, " en marcha ",
            self.enMarcha, " acelarar: ", self.acelar
        )


miVehiculo = Vehiculo("Audi", "Q10")
miVehiculo2 = Vehiculo("Mercedez Benz", "C10")
miVehiculo3 = Vehiculo("Ferrari", "Murcielago")
vehiculos = [miVehiculo, miVehiculo2, miVehiculo3]
fichero = open("LosVehiculos", "wb")
pickle.dump(vehiculos, fichero)
fichero.close()
del(fichero)
