"""FUNCION MAP"""
def calc_cuadrado(num):
    return (num**2)

numeros = [1,2,3,4,5,6,7,8,9,10]
print ("Numeros originales:", numeros, end="\n\n")

cuadrados = list( map( calc_cuadrado, numeros))
print("Con list(map()):", cuadrados)
# Lo que hace acá es con la función 'map()' aplicarle la funcion 'calcular_cuadrado' a cada elemento de la lista 'numeros'
# Como map lo que devuelve es un iterabe tipo 'map' con 'list()' lo convierto a lista

"""LISTAS POR COMPRENSIÓN (COMPREHENSION)"""
cuadradosComprehension = [num**2 for num in numeros]
print ("Por comprensión:", cuadradosComprehension)

# Esto es una forma más elegante de crear una lista sin utilizar un ciclo for de forma tradicional

"""LISTAS POR COMPRENSIÓN CON CONDICIONES"""
def es_par(num):
    return (num % 2 == 0)

cuadradosPares = [calc_cuadrado(num) for num in numeros if es_par(num)]
print ("Cuadrados pares:", cuadradosPares)

# De esta forma se agrega una condicion a la lista por comprensión, pero al ponerlo al final, no se puede poner 'else'

cuadradosResultados = [calc_cuadrado(num) if es_par(num) else 0 for num in numeros]
print("Cuadrados pares y ceros:", cuadradosResultados, end="\n\n")
# De esta forma (poniendo antes el 'if-else') podemos poner un else y así agregar más condiciones

"""SETS Y DICCIONARIOS"""
setPares = {num for num in numeros if num%2==0}
print("Set de Pares:", setPares)
# Es exactamente igual que con las listas, pero como se trata de un 'set' es entre llaves

dicCuadrados = {f"{num}": num**2 for num in numeros}
print("Diccionario de cuadrados:", dicCuadrados)

# Con diccionarios también es la misma lógica, pero indicando 'clave:valor'