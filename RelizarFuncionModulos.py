import math

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    return a / b

def raiz_cuadrada(x):
    if x < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        return None
    return math.sqrt(x)

def potencia(base, exponente):

    return base ** exponente
