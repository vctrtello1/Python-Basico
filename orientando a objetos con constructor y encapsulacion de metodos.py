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
            chequeo = self.__chequeoInterno()
        # realizamos el chequeo y si esta en lo correco
        # el vehiculo arranca
        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enMarcha and chequeo is False):
            return "Algo ha ido mal con el chequeo, no es posible arrancar"
        else:
            return "El coche esta apagado"

    def estado(self):
        # identacion correcta de un print
        print(
            "El coche tiene ", self.__ruedas, " ruedas, un ancho de ",
            self.__anchoChasis, " y un largo de  ",
            self.__largoChasis
        )

    def __chequeoInterno(self):
        print("Se va a realizar un chequeo interno")
        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if(
            self.gasolina == "Ok" and self.aceite == "Ok" and
            self.puertas == "Cerradas"
        ):
            return True
        else:
            return False


miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
# el metodo chequeo interno no es accesible desde afuera
# miCoche.__chequeoInterno() esto no es posible
print("A continuacion creamos el segundo objecto")
miCoche2 = Coche()
miCoche2.estado()
