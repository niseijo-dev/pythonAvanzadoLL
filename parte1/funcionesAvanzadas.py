# "*args" hace referencia a "non-keyword arguments" que son parámetros especiales usados para pasar parámetros opcionales en forma de tuplas cada posición
#  en la lista de ese parámetro será usado en la función.

# "**kwargs" significa "keyword arguments" son parámetros especiales usados para pasar parámetros opcionales en forma de diccionario.
#  Y como se envían como diccionario cada parámetro tiene un nombre asignado que sería la "key" del diccionario y el valor asociado

# El uso de " *args " se recomienda cuando no sabemos cuantos parámetros se nos pasará (y queremos recibirlos en forma de tuplas)

"""USO DE *args"""
def calc_perimetro(*args):
    perim = 0
    # Puedo imprimir args para ver que contiene
    #print("-- '*args' =", args)

    # Se puede iterar *args para utilizar cada parámetro
    for lado in args:
        perim += lado
    
    return perim

rectangulo = calc_perimetro(1,2,3,4) # Se envía de esta forma y la función recibe una tupla con los valores enviados
print("-- Perimetro del cuadrado =", rectangulo)
print("")

"""USO DE **kwargs"""
def func_kwargs(**kwargs):
    # Los parámetros se envían como "llave = valor" y kwargs los recibe como un diccionario
    print("++",kwargs)

    # Podemos iterarlo con un foreach de la siguiente forma
    for key, value in kwargs.items():
        print(f"++ K: {key}, V: {value}")
    
    # Como recibe los parámetros como un diccionario, puede usarse de la misma manera que uno cualquiera
    print("++",kwargs["nombre"], kwargs["apellido"])

func_kwargs(nombre = "Juan", apellido = "Pérez")

"""USO COMBINADO DE PARÁMETROS"""
# Primero se ponen los parámetros (normales), después *args y por último **kwargs
def param_ordenados(nombre, apellido, *args, **kwargs):
    print("No hay errores porque los parámetros están en orden")

"""
def param_desordenados(nombre, apellido, **kwargs, *args):
    print("Esta línea no se ejecutará porque dará error")
"""

param_ordenados("Nicolas", "Seijo") #*args y **kwargs son opcionales

"""FUNCIONES LAMBDA"""
# Son funciones anónimas y su sintaxis es: lambda argumentos: expresion
print ("## 2 * 2 es igual a:", (lambda x: x*2)(2)) # De esta forma la llamo y mando un parámetro directamente
producto = lambda num, mult: num * mult # De esta forma la asigno a una variable para reutilizarla
print("## 5 * 3 es igual a:", producto(5,3)) 

# Las funciones lambda pueden ser algo dificiles de leer, pero se recomienda su uso para enviarse como parametro en funciones como filter() o map()

# range(inicio, fin, paso)
