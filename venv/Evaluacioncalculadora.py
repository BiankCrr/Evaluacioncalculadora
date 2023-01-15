import numpy as np
import sys

def Suma(a, b):
    return np.sum(a + b)

def Resta(a, b):
    return a - b

def Multiplicación(a, b):
    return a * b

def Divición(a, b):
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
    print("4 Divición")
    print("5 Exponente")
    print("6 Raíz n")
    print("7 Seno")
    print("8 Coseno")
    print("9 Tangente")
    print("10 Salir de la Calculadora")

while True:
        num1 = 0
        num2 = 0
        num3 = 0
        choice = input("¿Que operación deseas realizar? (1\t2\t3\t4\t5\t6\t7\t8\t9\t10)")
        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Ingrese su primer número: "))
            num2 = float(input("Ingrese su segundo número: "))
        elif choice in ('7', '8', '9'):
            num3 = float(input("Ingresa un valor: "))
        if choice == '1':
            print(f"{num1} + {num2} = ", Suma(num1, num2))
        elif choice == '2':
            print(f"{num1} - {num2} = ", Resta(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} = ", Multiplicación(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} = ", Divición(num1, num2))
        elif choice == '5':
            print("La potencia es: ", Exponente(num1, num2))
        elif choice == '6':
            print("La raiz cuadrada del valor es: ", Raíz(num1, num2))
        elif choice == '7':
            print("El seno es: ", Seno(num3))
        elif choice == '8':
            print("El Coseno es", Coseno(num3))
        elif choice == '9':
            print("La tangente es", Tangente(num3))
        elif choice == '10':
            print("La calculadora se cerrará", Close())
        else:
            print("Su seleccion no es valida")
            break


EvaluacionCalculadora()