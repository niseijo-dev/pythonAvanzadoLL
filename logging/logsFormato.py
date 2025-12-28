import logging

logging.basicConfig( # Es obligatorio hacerlo al principio
   level=logging.DEBUG,
   format="%(asctime)s - %(levelname)s - %(message)s", # Se envia una cadena con un formato especial, la 's' final indica que es un string
   datefmt = "%H:%M:%S", # Acá defino como se verán las fechas en los logs, indiqué el formato HORA:MINUTOS:SEGUNDOS 
   filename="logsFormateados.log",
   filemode="w"
)

nombre = "Ejemplo"

logging.warning("ADVERTENCIA")
logging.error("ERROR")
logging.critical("ERROR CRÍTICO")

logging.error(f"{nombre} creó el error") # De esta forma puedo usar variables en un log
try:
    res = 5 / 0
except:
    logging.error("División por cero")