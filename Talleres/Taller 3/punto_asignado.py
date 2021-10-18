import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sy
from scipy.fft import fft, ifft

# funcion que evalua la expresion


def evaluar(x):
    return 1 / (1+25*x**2)


# creacion de los vectores donde se almacenaran los datos evaluados en la funcion
rango = np.arange(-1, 1, 0.1)
valores = []
valoresPol = []
# declaracion de variables y ecuaciones
v = sy.Symbol('v')
f = 1 / (1+25*v**2)

# calcular los valores por el tamaño del vector generado
for x in range(0, len(rango)):
    valores.append(evaluar(rango[x]))

# impresion de los datos
print("Los datos generador para el rango son: ")
print(rango)
print("Los datos obtenidos para los valores son de: ")
print(valores)

# implementacion del ruido usando Fourier
valoresPol = fft(valores)

# impresion de graficas de los datos
plt.plot(rango, valores, 'x--b', linewidth=0.5)
plt.plot(rango[0:7], valoresPol[0:7], 'x--r', linewidth=0.5)
plt.xlabel('Rango')
plt.ylabel('Valores evaluados en la funcion')
plt.show()
