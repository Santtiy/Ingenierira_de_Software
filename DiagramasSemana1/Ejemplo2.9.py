#Ejemplo2.9
class Empleado:
    def __init__(self, horas_trabajadas, pago_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
        
    def calcular_sueldo_semanal(self):
        return self.horas_trabajadas * self.pago_por_hora

horas = float(input("Ingrese el número de horas trabajadas: "))
pago = float(input("Ingrese el pago por hora: "))

empleado = Empleado(horas, pago)
sueldo_semanal = empleado.calcular_sueldo_semanal()
print(f"El sueldo semanal del empleado es: {sueldo_semanal:.2f}.")