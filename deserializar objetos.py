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


fichero = open("LosVehiculos", "rb")
misVehiculos = pickle.load(fichero)
fichero.close()
for i in misVehiculos:
    i.estado()
