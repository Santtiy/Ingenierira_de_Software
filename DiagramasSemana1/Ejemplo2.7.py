#Ejemplo2.7
class ProductorDeLeche:
    def __init__(self, cantidad_litros):
        self.cantidad_litros = cantidad_litros
        
    def convertir_a_galones(self):
        return self.cantidad_litros / 3.785
    
    def mostrar_galones(self):
        galones = self.convertir_a_galones()
        print(f"El productor de leche produce {galones:.2f} galones.")