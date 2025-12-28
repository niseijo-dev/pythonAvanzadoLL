# HTTP son las siglas de 'HyperText Transfer Protocol', es un protocolo de transferencia de datos para comunicación entre distintos servicios

# Una PETICIÓN (request) HTTP es un mensaje que se envía entre servicios para comunicarse. Inician acciones en los servicios
# Se componen por:  Línea de Inicio (tipo de petición), Headers (metadatos enviados) y Cuerpo (datos enviados si solicita cambiso en el servidor)
# El servidor envía RESPUESTAS HTTP, que se componen por: Linea de estado que contiene el protocolo y el código y texto de estado, también headers y cuerpo.
# Existen METODOS HTTP: GET (entrega de datos), POST (guardado de datos), PUT (Modificación de datos), DELETE (Eliminación de datos)

import requests

"""PETICIONES GET"""
response = requests.get("https://api.github.com")
print("# Respuesta:", response)

#print(response.headers) # Devuelve los headers
print("# Respuesta STATUS_CODE:", response.status_code) # Devuelve el estado de la respuesta

#print(response.content) # Devuelve la respuesta en bytes
#print(response.tex)t # Devuelve la respuesta como string
print("# Respuesta JSON:", response.json()["current_user_url"]) # Devuelve la respuesta como un diccionario, al que puedo acceder por sus claves.

"""USO DE PARAMS EN .get()"""
response = requests.get("https://api.github.com/search/repositories", params={"q":"python"}) # 'q' es query y buscará 'python'
# Las llaves son los parámetros de búsqueda y los valores son los parámetros que se usarán para realizar esa búsqueda

print((response.json()).keys())
