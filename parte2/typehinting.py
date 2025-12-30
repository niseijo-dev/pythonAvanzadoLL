# El type hinting es para asginarle un tipo estático a variables en Python, y se realiza como variable : tipo.
# El type hinting no modifica la ejecución del código, son como "anotaciones"

"""TYPE HINTING EN VARIABLES"""
nombre : str = "Juan"
edad : int = 25

pi : float = 3.1416

apellidos : list[str] = ["Perez", "Paez", "Pereyra"]
# Para las listas uso list, y si quiero aclarar el tipo lo pongo entre corchetes list[tipo]

lenguajesProgramacion : tuple[str, str, str, str] = ("python", "java", "javascript", "golang")
# Para las tuplas se declara el tipo de dato de cada variable
lenguaje : dict[str, str] = {"nombre":"python", "creador": "Guido Van Rossum"}
# Para los diccionarios si quiero aclarar el tipo es dict[tipoclave, tipovalor]

"""TYPE HINTING EN FUNCIONES"""
def perimetro_cuadrado(lado:int) -> int: # El -> int representa el tipo del que espero el retorno
    return 4*lado

perimetro_cuadrado("5")
# De la misma forma funciona con las clases de Programación Orientada a Objetos

# El type hinting son solo anotaciones, pero con la librería mypy (que se instala con pip install mypy) al ejecutar el archivo valida que los tipos sean los correctos
# Se usa igual que 'python' en la consola, por ejemplo "mypy typehinting.py". Al correrlo dará error en la línea 22.
# Para mi caso usé "python -m mypy typehinting.py" para que funcione el comando
    