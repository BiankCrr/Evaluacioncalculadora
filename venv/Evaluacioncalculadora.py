import numpy as np
import sys

def Suma(a, b):
    return np.sum(a + b)

def Resta(a, b):
    return a - b

def Multiplicación(a, b):
    return a * b

def Dividición(a, b):
    return a / b

def Raíz (a, b):
    return pow (a, 1/b)

def Exponente(a,b):
    return np.power(a,b)
def Seno (a):
    return np.sin (a)

def Coseno (a):
    return np.cos(a)

def Tangente(a):
    return np.tan (a)

def Close():
    sys.exit()
    
def Close():
    sys.exit()


def EvaluacionCalculadora():
    print("Buena vida, ¿Que operación deseas realizar?; ")
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicación")
    print("4 División")
    print("5 Exponente")
    print("6 Raíz n")
    print("7 Seno")
    print("8 Coseno")
    print("9 Tangente")
    print("10 Salir de la Calculadora")