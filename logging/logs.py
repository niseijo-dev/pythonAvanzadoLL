# El logging es el proceso de obtener 'logs' (registros) del programa. Estos indican la ocurrencia de eventos.
# Ayudan a entender el comportamiento del programa y así también encontrar errores.
# Los logs tienen niveles de seguridad: DEBUG, INFO, WARNING, ERROR y CRITICAL

import logging

logging.basicConfig(level=logging.DEBUG, filename="ejemploLogs.log", filemode="w") 
# Indica el nivel predeterminado de logging, por defecto es de WARNING para arriba. 
# Filename indica el nombre del archivo donde se guardan los logs. Filemode indica el modo en el que se abrirá, por defecto es 'a'

logging.debug("LOG de Debugging") # DEBUG para desarrollo
logging.info("LOG de INFO") # INFO para eventos de los que se requiere información
logging.warning("LOG de Advertencia") # WARNING indica algo inesperado sin que salte un error,
logging.error("LOG de Error") # ERROR es un reporte de algo que no se ejecutó porque hubo un error
logging.critical("LOG de Error Crítico") # CRITICAL es un informe de un error grave

# Se imprimen como NIVEL:Logger:Mensaje