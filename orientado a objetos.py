class Coche():

    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self, args):
        self.enMarcha = args
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"
        self.enMarcha = True

    def estado(self):
        # identacion correcta de un print
        print(
            "El coche tiene " + str(self.ruedas) + " ruedas, un ancho de "
            + str(self.anchoChasis) + " y un largo de  "
            + str(self.largoChasis)
        )


miCoche = Coche()
miCoche.arrancar(True)
miCoche.estado()

print("A continuacion creamos el segundo objecto")
miCoche2 = Coche()
miCoche2.estado()
