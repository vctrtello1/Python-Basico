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


class Furgoneta(Vehiculo):
    def carga(self, carga):
        self.cargado = carga
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class vehiculosElectricos(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargandoEnergia = True


# herencia de 2 clases diferentes
class BicicletaElectrica(vehiculosElectricos, Vehiculo):
    pass


class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "El caballito esta siendo realizo"
        return self.hcaballito
# sobreescritura de meotodo

    def estado(self):
        print(
            "Marca: ", self.marca, ", Modelo: ", self.modelo, " en marcha ",
            self.enMarcha, " acelarar: ", self.acelar,
            " caballito: ", self.hcaballito
        )
