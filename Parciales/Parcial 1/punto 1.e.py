import sympy as sy 
from sympy import *
import math
import numpy as np
from math import copysign, sqrt 
from mpmath import mp, mpf
import matplotlib.pyplot as plt

#implementacion del error hacia adelante y hacia atras
def errores(r1, r2, funcion,v ):
    errorHaciaAtras = abs(mpf(valorFuncion(funcion,r1)))
    errorHaciaAdelante = abs(mpf(r1 - r2))
    print("El error hacia atras es: " + str(errorHaciaAtras))
    print("El error hacia adelante es: " + str(errorHaciaAdelante))

# implementacion de metodo de Newton
def metodoNewton(v, e, funcion):
    
    #verificacion de que la funcion si tenga una seguda derivada
    if segundaDerivada(funcion) == 0:
        print("Error la funcion no tiene segunda derivada")
        return
    if derivada(funcion,v) == 0:
        print("Error la derivada de la funcion es cero")
        return
    #asignacion inicial del valor de la raiz
    r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    iteraciones = 0
    while abs(mpf(r - v)) > e:
        iteraciones = iteraciones + 1
        #validacion de un numero de iteraciones
        if iteraciones > 1000:
            arregloIteracionesNewton.append(0)
            return 0
        v = r
        #reasignacion de la raiz
        r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    print("El numero de iteraciones por Newton fue de: " + str(iteraciones))
    arregloIteracionesNewton.append(iteraciones)
    return mpf(r)
    
# funcion que evalua el valor de la funcion
def valorFuncion(funcion,v):
    return funcion.evalf(subs = {x:v}) 

import sympy as sy 
from sympy import *
import math
import numpy as np
from math import copysign, sqrt 
from mpmath import mp, mpf
import matplotlib.pyplot as plt

#implementacion del error hacia adelante y hacia atras
def errores(r1, r2, funcion,v ):
    errorHaciaAtras = abs(mpf(valorFuncion(funcion,r1)))
    errorHaciaAdelante = abs(mpf(r1 - r2))
    print("El error hacia atras es: " + str(errorHaciaAtras))
    print("El error hacia adelante es: " + str(errorHaciaAdelante))

# implementacion de metodo de Newton
def metodoNewton(v, e, funcion):
    
    #verificacion de que la funcion si tenga una seguda derivada
    if segundaDerivada(funcion) == 0:
        print("Error la funcion no tiene segunda derivada")
        return
    if derivada(funcion,v) == 0:
        print("Error la derivada de la funcion es cero")
        return
    #asignacion inicial del valor de la raiz
    r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    iteraciones = 0
    while abs(mpf(r - v)) > e:
        iteraciones = iteraciones + 1
        #validacion de un numero de iteraciones
        if iteraciones > 1000:
            arregloIteracionesNewton.append(0)
            return 0
        v = r
        #reasignacion de la raiz
        r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    print("El numero de iteraciones por Newton fue de: " + str(iteraciones))
    arregloIteracionesNewton.append(iteraciones)
    return mpf(r)
    
# funcion que evalua el valor de la funcion
def valorFuncion(funcion,v):
    return funcion.evalf(subs = {x:v}) 
#funcioin 2
def valorFuncion2(v):
    return  v**3 + 2*v + sqrt(1+2)
#funcioin3 
def valorFuncion3(v):
    return  v**3 + 2*v + (1-(1/3))

# funcion que calcula la derivada de la funcion 
def derivada(funcion, v):
    deriv = sy.diff(funcion,x)
    return deriv.doit().subs({x:v}).evalf()
def segundaDerivada(funcion):
    segunda = diff(funcion, x, 2)
    return segunda
#definicion de los parametros y de la funcion a calcular con K = numero de cedula

x = sy.Symbol('x')
funcion1 = x**3 + 2*x + sqrt(1+2)
funcion2 = x**3 + 2*x + (1-(1/3))
arregloIteracionesNewton = []
#impresion de el dato al inicial para la funcion de newton
valor = input("Ingrese el valor inicial para Newton: ")

#ejecucion de las funciones
mp.dps = 12
print("---------------------------------------")
print("En la funcion funcion 1 el resultado fue:")
r1 = mpf(metodoNewton(mpf(valor), mpf(1.0e-12), funcion1))
print("---------------------------------------")
print("En la funcion funcion 2 el resultado fue:")
r2 = mpf(metodoNewton(mpf(valor), mpf(1.0e-12), funcion2))
print("raiz = " + str(r1))
print("raiz = " + str(r2))
print("-----------------Errores---------------")
print("En la funcion funcion 1 el error fue:")
errores(r1,r2,funcion1,valor)
print("En la funcion funcion 2 el error fue:")
errores(r1,r2,funcion2,valor)

u = np.linspace(-1,1,50) 
# graficacion
plt.plot(u,valorFuncion2(u))
plt.plot(u,valorFuncion3(u))
plt.grid()
plt.title('Convergencia de la funcion')
plt.show()    