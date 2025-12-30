import time
"""CONCEPTO DE CLOSURE"""
# Un "closure" es una función anidada (es decir declarada de otra función 'padre') que hace uso de variables de la función que la contiene.
# Al mismo tiempo, esa función es retornada por su función padre.
# Sirve para no crear clases cortas donde solo hay un método

def agregar_persona_directorio(): # Funcion 'padre' o 'principal'
    directorio = {}
    def agregar(nombre, edad, ciudad): # Declara la función anidada
        directorio[nombre] = {"edad": edad, "ciudad": ciudad}
        return directorio
    return agregar # Retorna la función anidada

almacenar = agregar_persona_directorio() # La función principal retorna la función, por lo que se lo asigno a una variable que tendrá la función retornada
direc = almacenar("Juan", 33, "CABA")
print(direc)

"""DECORADORES"""
# Son funciones que reciben como parámetro otra función, le agrega más funcionalidades y retorna la función modificada
# Un decorador se declara de la misma forma que un closure pero debe recibir una función para ser considerado decorador

def fc_decorador(funcion):
    def fc_wrapper(): # La función anidada en decoradores se llama 'wrapper' que significa envolver, ya que envuelve y modifica la función recibida
        print("Dentro de función wrapper")
        funcion()
    return fc_wrapper

"""def fc_prueba():
     print("Esto es una función de prueba")""" # Descartada por lineas posteriores

""" fc_prueba = fc_decorador(fc_prueba) """ # Descartada por lineas posteriores

"""FORMA PYTHONICA DE DECORAR"""
@fc_decorador
def fc_prueba():
    print("Funcion de prueba")

# De esta forma las líneas 27 a 31 se descartan

fc_prueba()

"""EJEMPLO PRÁCTICO: FUNCION CON PARÁMETROS"""
def tiempo_ejecucion(funcion):
    def wrapper(*arg, **kwargs): # Se utiliza *arg y **kwargs para que cualquier función con cualquier cantidad de argumentos pueda ser ejecutada
        inicio = time.time()
        funcion(*arg, **kwargs) # El wrapper los recibe y los envia a la función, recordemos que *arg y **kwargs son opcionales
        print (f"Tiempo total de ejecución: {(time.time()) - inicio}")
    return wrapper

"""MULTIPLES DECORADORES"""
def agregar_puntos(funcion):
    def wrapper(*arg, **kwargs):
        print(".........") 
        funcion(*arg, **kwargs)
        print(".........") 
    return wrapper

@agregar_puntos # El orden de los decoradores importan, de esta forma tiempo_ejecucion decora la función y agregar_puntos decora la función decorada por la anterior
@tiempo_ejecucion # Si invirtiera el orden, el tiempo de ejecución se mediría incluyendo la impresión de agregar_puntos
def recorrer_ciclo(rango):
    for i in range (rango):
        print(i+1, end=" ")
        time.sleep(1) # Espera 1 segundo

recorrer_ciclo(5)

# Los decoradores son utilizados por múltiples librerías como Flask o Selenium