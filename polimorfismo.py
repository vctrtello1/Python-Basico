class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo con 8 ruedas")


# ejemplo de polimorfismo
def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()


miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
