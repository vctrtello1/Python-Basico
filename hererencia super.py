class persona():
    def __init__(self, nombre, edad, lugarDeResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarDeResidencia = lugarDeResidencia

    def descripcion(self):
        print(
            "Nombre: ", self.nombre, " edad: ", self.edad,
            ", lugar de residencia ", self.lugarDeResidencia
        )


class empleado(persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugarDeResidencia):
        # metodo super para herencia
        super().__init__(nombre, edad, lugarDeResidencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(", salario", self.salario, " ,antiguedad", self.antiguedad)


# principio de sustitucion
# primerPersona = persona("Antonio", 55, "Mexico")
Antonio = empleado(1500, 15, "Antonio", 55, "Mexico")
Antonio.descripcion()
# determinar si es Instancia de la clase empleado
print(isinstance(Antonio, empleado))
# comprobar si es de tipo persona
print(isinstance(Antonio, persona))
Manuel = persona("Manuel", 22, "España")
# instaciar de otra manera
print(isinstance(Manuel, persona))
print(isinstance(Manuel, empleado))
