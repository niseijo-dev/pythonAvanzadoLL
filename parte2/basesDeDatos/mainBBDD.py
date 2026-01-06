from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session

"""CREAR DATOS EN BASE DE DATOS CON SQLALCHEMY"""
def guardar_datos():
    """DEPARTAMENTOS"""
    contabilidad = Departamento("Contabilidad") # Creamos el departamento
    session.add(contabilidad) # Con 'session.add()' agrego

    it = Departamento("IT")
    session.add(it)

    session.commit() # Esto sube los cambios a la BBDD, enviando la orden de "COMMIT", similar a como funciona 'GIT'
    # Lo hago antes de crear los empleados para que los departamentos existan

    """EMPLEADOS"""
    carlos = Empleado("Carlos", "Diaz", 14755236, contabilidad.id) # contabilidad.id es la clave foránea
    session.add(carlos)

    juan = Empleado("Juan", "Perez", 12344567, it.id)
    session.add(juan)

    session.commit() # Vuelvo a subir los cambios 

    print("ID CONTABILIDAD:", contabilidad.id)

"""REALIZAR CONSULTAS EN LA BASE DE DATOS CON SQLALCHEMY"""
def hacer_consultas():
    departamento1 = session.get(Departamento, 1) # .get nos permite 'traer' un elemento, se le pasa el Modelo y el id
    print(departamento1) # Esto nos devuelve algo no legible, por lo que necesitamos definir los 'dunder method's de los modelos (__str__)

    cantDepartamento = session.query(Departamento).count()
    #.query() es equivalente a un SELECT, se le pueden anidar más métodos para construir una consulta como en SQL
    print("Hay", cantDepartamento, "departamentos")

    empleadosCont = session.query(Empleado).filter_by(idDep=departamento1.id).all()
    # Esto sería SELECT * FROM EMPLEADO WHERE idDep = <valor de departamento1.id>
    # Y nos retornaría una lista de Modelos "Empleado" por lo que hay que iterar para imprimir
    print("EMPLEADOS:")
    for empleado in empleadosCont:
        print(empleado)

"""MAIN"""
if __name__ == "__main__": # Esto correrá solo si el archivo se esta ejecutando como main, no importado
    ModeloBase.metadata.create_all(engine) # Esto crea todas las tablas en la BBDD
    # guardar_datos() # Llamo a la función guardar_datos para crear los departamentos y empleados
    hacer_consultas()

# NOTA: Los resultados de correr este archivo se verán en la base de datos utilizando la extensión SQLITE VIEWER

