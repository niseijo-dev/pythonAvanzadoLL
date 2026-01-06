# Los modelos son las tablas de la BBDD, se representan con clases.
from conexion import ModeloBase # Se importa el modelo base, todos los modelos serán clases de Python, pero seran clases hijas del modelo base.

from sqlalchemy import Column, Integer, String, ForeignKey # Se debe importar que es una columna y el tipo de dato para cada atributo del modelo

class Departamento(ModeloBase):
    __tablename__ = "departamento"
    
    id = Column(Integer, primary_key = True) # Indicamos que es un atributo identificador DE LA TABLA
    nombre = Column(String, nullable = False, unique = True) #Nullable es si puede o no ser nulo (en este caso no), unique es que no puede haber repetidos

    def __init__ (self, _nombre): # Defino el constructor de la clase, se le ingresa nombre
        self.nombre = _nombre 

    def __str__ (self):
        return f"{self.id} | {self.nombre}"

class Empleado(ModeloBase):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable = False)
    apellido = Column(String, nullable = False)
    dni = Column(String, nullable = False, unique=True)
    idDep = Column(Integer, ForeignKey("departamento.id")) 
    # Para usar una FK importamos 'ForeingKey' de sqlalchemy y le indicamos con un string usando el tablename de la tabla foránea

    def __init__ (self, _nombre, _apellido, _dni, _idDep):
        self.nombre = _nombre
        self.apellido = _apellido
        self.dni = _dni
        self.idDep = _idDep

    def __str__ (self):
        return f"{self.id} | {self.nombre} {self.apellido}"
