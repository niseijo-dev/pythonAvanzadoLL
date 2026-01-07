import unittest # Para las pruebas unitarias usaremos unittest

def es_primo(num): # Esta es una función para 'testear' que verifica si un número es primo o no
    if num <= 1:
        return False
    
    for i in range (2, num):
        if num % i == 0:
            return False
        
    return True

class Test(unittest.TestCase): # Para hacer las pruebas en unitest, se crea una clase Test() que es hija de TestCase de la librería
    def test_menor_igual_uno(self): # Para que los métodos se reconozcan como pruebas su nombre debe comenzar con 'test_'
        resultado = es_primo(1)
        self.assertTrue(resultado) # Con .assertFalse() comprobamos que el resultado sea 'False'

    def test_no_primo(self):
        resultado = es_primo(4)
        self.assertEqual(False, resultado) # .assertEqual verifica que dos variables tengan el mismo valor

    def test_primo(self):
        resultado = es_primo(3)
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()