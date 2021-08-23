import numpy as np
import matplotlib.pyplot as plt
import math

def f1(x):
    if 1-x == 0:
        return math.inf 
    else:
        return 1/(1-float(x))


valorInicio = input("ingrese el valor inicial del rango: ")
valorFinal = input("ingrese el valor final del rango: ")
numeros = input("ingrese el valor de cuantos numeros se quieren: ")

rango = np.linspace(int(valorInicio), int(valorFinal), int(numeros)) # se crean los valores en el rango 

lista = []

for numero in rango:
    valor = f1(numero)
    lista.append(float(valor))

print("----- Valores Rango ------")

for i in range(0, len(rango)):
    print(str(i) + ": " + str(rango[i]))

print("----- Valores Aproximacion ------")

for i in range(0, len(lista)):
    print(str(i) + ": " + str(lista[i]))

print("----- Valores Taylor ------")

# graficacion
plt.plot(rango, lista, color = "red")
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor 1/(1-x)')
  
plt.show()    


