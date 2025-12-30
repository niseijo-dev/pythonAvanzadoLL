# Por convención las clases en Python se escriben como UpperCamelCase
# NOTA: Ya tengo conocimientos de Programación Orientada a Objetos por lo que mi aprendizaje se basará más en como se aplica para el lenguaje Python.

"""CONCEPTOS INICIALES DE P.O.O EN PYTHON"""
class Persona:
    tipo = "humano" # Esto es un atributo, pero normalmente se declara en el constructor __init__

    def __init__ (self, nombre, apellido, edad): # Este es el constructor, Python no admite sobrecarga como en Java o C#
        # 'self' representa la instancia de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.docIdentidad = None

    def agregar_documento(self, docIdentidad): # Esto es un método, en este caso un setter para docIdentidad
        self.docIdentidad = docIdentidad
        print(f"Documento: [{docIdentidad}] guardado exitosamente.")

    def accion(self):
        print("Haciendo algo...")

juanPerez = Persona("Juan", "Perez", 33)
juanPerez.agregar_documento(30822335)
#print(juan.tipo)

"""HERENCIA"""
class Deportista(Persona): # De esta forma se le asigna 'Persona' como clase padre
    def __init__(self, nombre, apellido, edad, deporte):
        Persona.__init__(self, nombre, apellido, edad) # Llamo al constructor de persona
        # Usando super().__init__() también funciona ya que super() referencia a la clase padre.
        self.deporte = deporte

    def accion(self): # Acá aparece la herencia
        super().accion() # Llamo al método de la clase padre, sea con super() o con el mismo nombre de la clase, para que se ejecute primero
        print(f"Practicando {self.deporte}...") # Posteriormente agrego las acciones que implementará adicionalmente la clase hija

goat = Deportista("Lionel Andrés", "Messi Cuccittini", 38, "Fútbol") # Utilizo el constructor de clase Persona (herencia)
goat.agregar_documento(33016244) # También sus métodos
goat.accion()

"""HERENCIA MULTIPLE"""
class AnimalAereo():
    def comer(self): print("Animal aéreo comiendo...")

    def volar(self): print("Volando...")

class AnimalTerreste():
    def comer(self): print("Animal terrestre comiendo...")

    def caminar(self): print("Caminando...")

class Pajaro(AnimalAereo, AnimalTerreste):
    pass

pato = Pajaro()
pato.volar()
pato.caminar()
pato.comer() # Acá va a usar el método de 'AnimalAereo' ya que Python cuando hay dos métodos con el mismo nombre usa el de la primera clase definida. (MRO)
