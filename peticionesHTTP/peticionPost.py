import requests
# Generalmente la información enviada en un POST se almacena en una base de datos ligada al servidor.

url = "https://webhook.site/a0dc136d-0aca-4d7b-b265-4b57c5303ab1"
payload = {"plato":"pasta", "cantidad":"2"} # Payload significa carga y son los datos que voy a enviar
queryParams = {"nombre":"Juan"}

response = requests.post(url, data=payload, params=queryParams)

print(response.status_code)
print(response.text) # Como la URL no devuelve nada, si uso response.json() saltará error