class Coche():
    # el constructor debe tener dos guiones bajos
    # en ambos lados __ init __ para que funcione
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, args):
        self.__enMarcha = args
        if(self.__enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"

    def estado(self):
        # identacion correcta de un print
        print(
            "El coche tiene ", self.__ruedas, " ruedas, un ancho de ",
            self.__anchoChasis, " y un largo de  ",
            self.__largoChasis
        )


miCoche = Coche()
miCoche.arrancar(True)
miCoche.estado()

print("A continuacion creamos el segundo objecto")
miCoche2 = Coche()
miCoche2.estado()
