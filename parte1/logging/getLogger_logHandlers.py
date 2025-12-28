import logging

"""LOGGER PERSONALIZADOS"""
# Se puede modificar el logger para que no sea necesariamente 'root'
logger = logging.getLogger(__name__) # Con este método le asignamos un nuevo logger a la variable homónima
# Se recomienda poner '__name__' como parámetro ya que esto le pondrá el nombre del paquete o módulo en el que se esté trabajando

logger.warning("ADVERTENCIA") # Como el logger ya no es 'root' el formato será solo el mensaje (por defecto)

"""LOGGER HANDLERS"""
# Los logger handlers permiten configurar y personalizar los loggers
logger.setLevel(logging.DEBUG)

# Los más comunes son StreamHandler (consola) y FileHandler (Archivos), pero existen más
handlerConsola = logging.StreamHandler()

# Usando handlers no se puede usar .basicConfig() por lo que para aplicar formatos usamos el objeto Formatter
formato = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handlerConsola.setFormatter(formato) # Y lo aplicamos al handler con el método .setFormatter()
logger.addHandler(handlerConsola) # Con .addHandler se le aplica el handler al logger

handlerArchivo = logging.FileHandler("logsConHandler.log")
handlerArchivo.setLevel(logging.ERROR)
handlerArchivo.setFormatter(formato)
logger.addHandler(handlerArchivo)

logger.info("REGISTRO INFORMATIVO")
logger.error("REGISTRO DE ERROR")