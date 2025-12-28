import pdb # Librería para hacer debugging

def area_cuadrado(lado):
    """Calcula el área de un cuadrado recibiendo la longitud de un lado"""
    area = lado*lado
    return area

ladosCuadrado = [1, 3, 5]
areasCuadrado = []

for lado in ladosCuadrado:
    area = area_cuadrado(lado)
    areasCuadrado.append(area)