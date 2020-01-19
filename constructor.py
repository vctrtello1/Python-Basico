class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.ruedas = 4
        self.__enMarcha = False

    def estado(self):
        print(self.ruedas)


miCoche = Coche()

miCoche.estado()
