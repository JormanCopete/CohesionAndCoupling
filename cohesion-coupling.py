import string 
import random

class InformacionVehiculo:
    marca: string
    precio: int
    electrico: bool
    
    def __init__(self, marca, electrico, precio):
        self.marca = marca
        self.precio = precio
        self.electrico = electrico
        
    def calcule_impuesto(self):
        porcentaje_impuesto = 0.05
        if self.electrico:
            porcentaje_impuesto = 0.02
        return porcentaje_impuesto * self.precio
    
    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Impuesto a pagar: {self.calcule_impuesto()}")
        
class Vehiculo:
    id: string
    placa:string
    informacion: InformacionVehiculo
    
    def __init__(self, id, placa, informacion):
        self.id = id
        self.placa = placa
        self.informacion = informacion
    
    def imprimir(self):
        print(f"ID: {self.id}")
        print(f"Placa: {self.placa}")
        self.informacion.imprimir()
        
        
class RegistroDeVehiculo:
    
    informacion_vehiculo = {}
    
    def add_informacion_vehiculo(self, marca, electrico, precio):
        self.informacion_vehiculo[marca] = InformacionVehiculo(marca, electrico, precio)
        
    def __init__(self):
        self.add_informacion_vehiculo("Tesla Model 3", True, 60000)
        self.add_informacion_vehiculo("Wolkswagen ID3", True, 35000)
        self.add_informacion_vehiculo("BMW 5", False, 45000)
        self.add_informacion_vehiculo("Wolkswagen ID3Tesla Model Y", True, 75000)
        
    def generar_identificacion_vehiculo(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
        
    def generar_licencia_vehiculo(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2 ))}"    
    
    def crear_vehiculo(self, marca):
        id_vehiculo = self.generar_identificacion_vehiculo(12)
        placa = self.generar_licencia_vehiculo(id_vehiculo)
        return Vehiculo(id_vehiculo, placa, self.informacion_vehiculo[marca])
    
    
class Application:
    
    def registrar_vehiculo(self, marca: string):
        registro = RegistroDeVehiculo()
        return registro.crear_vehiculo(marca)
    
    
app = Application()
vehiculo = app.registrar_vehiculo("Wolkswagen ID3")
vehiculo.imprimir()
        
        
        