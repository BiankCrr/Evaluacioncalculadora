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

def Raiz (a, b):
    return pow (a, 1/b)

def Exponente(a,b):
    return np.power(a,b)
#def Seno (a):
    #return np sin (a)

#def Coseno (a):
    #return np cos (a)

def Tangente(a):
    return np.tan(a)

def Close():
    sys.exit()