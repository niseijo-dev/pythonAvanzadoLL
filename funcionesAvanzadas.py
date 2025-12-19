def calc_perimetro(*args):
    perim = 0
    # Puedo imprimir args para ver que contiene
    print("-- '*args' =", args)

    # Se puede iterar *args para utilizar cada parámetro
    for lado in args:
        perim += lado
    
    return perim


perimetro = calc_perimetro(1,2,3,4) # Se envía de esta forma y la función recibe una tupla con los valores enviados
print("-- Perimetro =", perimetro)