"""SOBRECARGA DE OPERADORES"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.distanciaRec = 0

    def __add__ (self, distancia): # __add__ es el 'dunder method' que modifica la suma
        self.distanciaRec += distancia
        return self.distanciaRec
    
    def __lt__(self, otraPersona): # Este es el dunder method que modifica < (menor que)
        return (self.edad < otraPersona.edad)

juan = Persona("Juan", 22)
pedro = Persona("Pedro", 19)

juan + 5
print(f"Distancia recorrida por {juan.nombre}: {juan.distanciaRec}")

print("¿Pedro es menor a Juan?. Respuesta:", pedro < juan)

