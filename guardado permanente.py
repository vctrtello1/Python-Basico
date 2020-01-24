import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

# metodo especial para convertir a texto
    def __str__(self):
        # dar fomrato a la cadena
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        # revisar carga de fichero externo ya que no se se esta realizando
        # abrir fichero para guardar infomracion binaria
        listaDePersonas = open("ficheroExterno", "ab+")
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se ha cargado la informacion de manera correcta")

        except Exception:
            print("El fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, persona):
        self.personas.append(persona)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for i in self.personas:
            print(i)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        del(listaDePersonas)

    def mostarInformacionDeFicheroExterno(self):
        print("La informacion de fichero externo es la siguiente")
        for i in self.personas:
            print(i)


miListaPersonas = ListaPersonas()
miPersona = Persona("Victor", "Masculino", 27)
miListaPersonas.agregarPersonas(miPersona)
miListaPersonas.mostarInformacionDeFicheroExterno()
miPersona2 = Persona("Hugo", "Masculino", 28)
miListaPersonas.agregarPersonas(miPersona2)
miPersona3 = Persona("Tello", "Masculino", 29)
miListaPersonas.agregarPersonas(miPersona3)
miPersona4 = Persona("Miramones", "Masculino", 30)
miListaPersonas.agregarPersonas(miPersona4)
miListaPersonas.mostrarPersonas()
