# NOTA: Este concepto es ya conocido por lo que habrán menos notas explicativas
import json

"""ESCRIBIR JSON"""
persona = {
    "nombre":"Claudio",
    "apellido":"Gomez",
    "edad": 52 
}

"""objetoJson = json.dumps(persona, indent=2)""" # Esta función serializa a JSON. 'indent = 2' establece el indentado

with open("personas.json", "w") as arch:
    """arch.write(objetoJson)""" # De esta forma escribo directamente el archivo serializado
    json.dump(persona, arch) # De esta forma escribo directamente al archivo JSON sin necesidad de serializar, pero no tendrá el indentado

"""LEER JSON"""
with open("personas.json", "r") as arch:
    datosJson = json.load(arch) # Con esta funcion recibo los datos como diccionario o lista (depende del Json)

print(datosJson)
print(datosJson["nombre"])  # Como es un diccionario puedo acceder a los datos como cualquier otro