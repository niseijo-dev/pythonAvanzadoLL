# CSV significa "Comma Separated Values" osea "Valores Separados con Coma" y es un tipo de archivo que nos permite almacenar datos fácilmente.
# Los datos almacenados en CSV representan tablas, donde cada valor separado con coma representa una columna y cada línea del archivo es una fila
import csv

"""CREAR ARCHIVO CSV"""
path = "arch_vacio.csv"

arch = open(path, "w") # Apertura del archivo en modo escritura
writer = csv.writer(arch, delimiter=",") 
# Esta función nos permite escribir sobre el archivo .csv y se asigna por convención a la variable "writer"
arch.close()

"""ESCRIBIR SOBRE ARCHIVO CSV"""
columnas = ["nombre", "apellido", "edad"]

matrizDatos = [
    ["Juan","Nadie",20],
    ["John","Doe",32]
]

with open("datos.csv", "w", newline="") as arch: # Esta es otra forma de abrir un archivo. 'newline="" ' sirve para que no agregen lineas vacías
    # Dentro de este bloque "with se abre y cierra el archivo sin un .close()"
    writer = csv.writer(arch,delimiter=",")

    writer.writerow(columnas)
    writer.writerow(["Pedro", "Perez", 40])
    # .writerow() escribe una sola línea en el archivo .csv
    writer.writerows(matrizDatos)
    # .writerows() nos permite hacerlo con listas de listas para escribir múltiples filas

"""ESCRIBIR CON DICCIONARIOS"""
listaDatos = [
    {"nombre":"Pablo", "apellido":"Paez", "edad": 33},
    {"nombre":"Nicolas", "apellido":"Seijo", "edad": 23}
]

with open("datos.csv", "w",  newline="") as arch:
    writer = csv.DictWriter(arch, fieldnames=columnas)
    # csv.DictWriter() es un método especial que nos ayuda a manejar diccionarios
    # El atributo 'fieldnames' son las columnas del archivo .csv por lo que se le envía la lista 'columnas'
    writer.writeheader()
    # .writeheader() escribe en la primera línea los encabezados
    writer.writerows(listaDatos)

"""LEER ARCHIVOS CSV"""
with open("datos.csv", "r", encoding="UTF-8") as arch:
    reader = csv.reader(arch) # csv.reader() es un método que se utiliza para obtener un "lector" de archivos (por convención: reader)
    columnas = next(reader) # Esta función nos permite "avanzar" a la siguiente línea y devuelve la línea 'salteada'
    print("Columnas:", columnas)
    for fila in reader:
        print(fila)
    print("")

"""LEER COMO DICCIONARIOS"""
with open("datos.csv", "r", encoding="UTF-8") as arch:
    reader = csv.DictReader(arch)
    for fila in reader:
        print("NOMBRE:", fila["nombre"])
        print("APELLIDO:", fila["apellido"])
        print("EDAD:", fila["edad"])
        print("")