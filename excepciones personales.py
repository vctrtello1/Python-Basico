# manejo de excepciones propias con el metodo Raise
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("Burroooo")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"


print(evaluaEdad(-12))
