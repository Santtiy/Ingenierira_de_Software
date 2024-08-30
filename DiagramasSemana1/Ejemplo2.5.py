#Ejemplo2.5
class TerrenoFormaA:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

baseDelTerreno = float(input("Ingresa la longitud de la base del terreno (En unidades): "))
alturaDelTerreno = float(input("Ingresa la altura del terreno (En unidades): "))

terreno = TerrenoFormaA(baseDelTerreno, alturaDelTerreno)
area = terreno.calcular_area()
print(f"El área del terreno con forma A es: {area} unidades cuadradas.")



