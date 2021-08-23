import math
from math import copysign 

def metodoBiseccion(a,b,e):

    sign = lambda x : copysign(1, x) # variable que dice si el signo de un valor es negatibo (-1) o si es positivo (1)
    iteraciones = 0
    while b - a > e:
        c = (a+b)/2
        if funcion(c) == 0: 
            return round(c,4)
        else:
            if sign(funcion(c)) == sign(funcion(a)):
                a = c
            else:
                b = c
        iteraciones += 1
    print("El numero de iteraciones fue de: " + str(iteraciones))
    return round((a+b)/2, 4) 

def funcion(x):
    valor = x * (math.e**x) - math.pi # funcion (x * e^x - pi) de prueba que esta en el libro ANALISIS NUMERICO BASICO
    return valor

def validacion(x):
    valor = x * (math.e**x) - math.pi # funcion (x * e^x - pi) de prueba que esta en el libro ANALISIS NUMERICO BASICO
    return valor


e = input("Ingrese el valor del error: ")
a = input("Ingrese el valor inicial del intervalo: ") 
b = input("Ingrese el valor final del intervalo: ") 

print(metodoBiseccion(float(a),float(b),float(e)))

x = 1.0737
print(validacion(x))