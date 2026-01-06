# En Python se utiliza programación secuencial, cada línea se ejecuta DESPUES de la anterior
# En la programación asíncrona o recurrente cada instrucción inicia su ejecución al mismo tiempo
# La asíncrona tarda menos en ejecutar las tareas, en este curso se usará la librería AsyncIO para implementarla

import time, asyncio # Asyncio no requiere instalación

def funcion_sincrona():
    print("Ejecutando función síncrona")
    time.sleep(1)
    print("Fin de la función síncrona")

async def funcion_asincrona(): #Se definen funciones asíncronas con 'async' antes de 'def...'
    print("Ejecutando función asíncrona")
    await asyncio.sleep(1) # 'await' hace una pausa hasta que se obtenga el resultado
    print("Fin función asíncrona")

# Para ejecutar las funciones asíncronas es buena práctica crear una función "padre" que gestione las co-rrutinas, llamada por convención 'main()'

async def main():
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    await asyncio.gather(*corrutinas)

asyncio.run(main())