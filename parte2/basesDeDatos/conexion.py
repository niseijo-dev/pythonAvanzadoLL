# Para trabajar en BBDD SQL en Python se usan 'ORM', librerías especializadas para manipular BBDDs
# 'ORM' significa 'Object Relational Mapper', permite manipular una BBDD y sus tablas como si fueran objetos.
# Una tabla es representada por una Clase (Class) y también se la llama MODELO donde cada columna es un atributo de la clase y cada fila es una instancia de ella.
# 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

nombreDB = "empleados.sqlite"
engine = create_engine(f"sqlite:///{nombreDB}") # Recibe el nombre de la Base de Datos en el formato de SQLite
# Al crear el 'engine' no se esta creando la conexión, esta se creará cuando la variable sea usada por primera vez en el código

# La sesión es el conj. de operaciones de comunicación con la base de datos, por medio de ella podemos leer, escribir, modificar y eliminar datos de la BBDD
Session = sessionmaker(bind=engine)
session = Session()
# Con esto ya se puede trabajar con la base de datos.

ModeloBase = declarative_base()