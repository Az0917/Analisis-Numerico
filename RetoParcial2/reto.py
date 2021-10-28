from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
# definicion de arreglos globales
hora_inter = []
temp_inter = []
hora_inter_2 = []
temp_inter_2 = []
hora_inter_3 = []
temp_inter_3 = []

# inicializacion de los arreglos
hora = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

arreglo_indices = np.arange(1, 721).tolist()
hora_30 = np.arange(1, 721).tolist()
temperatura_inicial = []
temperatura_inicial_aux = []
temperatura_30 = []
registros_eliminados = []


# calcular valores por interpolacion
def inter(hora_v, temperatura):
    interpolacion_hora_temp = interpolate.interp1d(hora_v, temperatura)

    i = hora_v[0]
    for x in range(0, (len(arreglo_indices)-1)*2):
        hora_inter.append(i)
        temp_inter.append(interpolacion_hora_temp(i))
        i = i + 0.5

# calcular valores por interpolacion cuadratica


def inter_cuadratica(hora_v, temperatura):
    interpolacion_hora_temp_2 = interpolate.interp1d(
        hora_v, temperatura, kind="cubic")
    i = hora_v[0]
    for x in range(0, (len(arreglo_indices)-1)*2):
        hora_inter_2.append(i)
        temp_inter_2.append(interpolacion_hora_temp_2(i))
        i = i + 0.5

# inter cuadrada con estacion cercana


def inter_cuadratica_cercana(hora_v, temperatura):
    interpolacion_hora_temp_3 = interpolate.interp1d(
        hora_v, temperatura, kind="cubic")
    i = hora_v[0]
    for x in range(0, (len(arreglo_indices)-1)*2):
        hora_inter_3.append(i)
        temp_inter_3.append(interpolacion_hora_temp_3(i))
        i = i + 0.5

# esta funcion se encarga de tomar los datos de la tempreratura del excel en un dia juliano en especifico


def cargar_excel():
    excel = pd.read_excel(
        "D:\Carpetas Windows\documentos\GitHub\Analisis Numerico\Reto Parcial 2\Base_datos.xls", sheet_name='Itatira')

    excel = excel[["Temp. Interna (ºC)"]]
    return excel.to_numpy()

# esta funcion carga los datos de una estacion cercana


def cargar_excel2():
    excel = pd.read_excel(
        "D:\Carpetas Windows\documentos\GitHub\Analisis Numerico\Reto Parcial 2\Base_datos.xls", sheet_name='Quixadá')

    excel = excel[["Temp. Interna (ºC)"]]
    return excel.to_numpy()


# impresion de graficas de los datos
def imprimir_resultados():
    plt.plot(arreglo_indices, temperatura_inicial, '-k',
             linewidth=2, label="Datos Originales")
    plt.plot(hora_inter, temp_inter, '-g',
             linewidth=1, label="Interpolacion Lineal")
    plt.plot(hora_inter_2, temp_inter_2, '-r',
             linewidth=1, label="Interpolacion cuadratica")
    plt.xlabel('Registro de hora')
    plt.ylabel('Temperatura interna (c)')
    plt.legend()
    plt.show()


def imprimir_estacion_cercaan():
    plt.plot(arreglo_indices, temperatura_inicial, '-k',
             linewidth=2, label="Datos Originales")
    plt.plot(hora_inter_3, temp_inter_3, '-r',
             linewidth=1, label="Interpolacion cuadratica con estacion cercana")
    plt.xlabel('Registro de hora')
    plt.ylabel('Temperatura interna (c)')
    plt.legend()
    plt.show()


# asignacion del arreglo de los datos obtenidos por el excel
validacion = 0
validacion2 = 0
diferenciaMax = float("-inf")
diferenciaMin = float("inf")
valorMaximo = 0
valorMinimo = 0
diferenciaMax2 = float("-inf")
diferenciaMin2 = float("inf")
valorMaximo2 = 0
valorMinimo2 = 0

arreglo = cargar_excel()
for x in arreglo:
    temperatura_inicial.append(x.item())

arreglo2 = cargar_excel2()
for x in arreglo2:
    temperatura_inicial_aux.append(x.item())

temperatura_30 = temperatura_inicial.copy()
# eliminacion de los datos 30%
datos_eliminar_num = (int)(len(temperatura_inicial) * 0.30)
for i in range(0, datos_eliminar_num):
    posicion = random.randrange(1, len(temperatura_30)-1)
    temperatura_30.pop(posicion)
    registros_eliminados.append(hora_30[posicion])
    hora_30.pop(posicion)


# calculo de la interpolaciones
inter(hora_30, temperatura_30)
inter_cuadratica(hora_30, temperatura_30)
inter_cuadratica_cercana(arreglo_indices, temperatura_inicial_aux)


# calculo de error cuadratico medio
for i in range(0, len(registros_eliminados)):
    validacion = validacion + (temp_inter_2[i*2] - temperatura_inicial[i])**2
    validacion2 = validacion2 + (temp_inter[i*2] - temperatura_inicial[i])**2
    if diferenciaMax < temp_inter_2[i*2] - temperatura_inicial[i]:
        diferenciaMax = temp_inter_2[i*2] - temperatura_inicial[i]
        valorMaximo = temperatura_inicial[i]
    if diferenciaMin > temp_inter_2[i*2] - temperatura_inicial[i]:
        diferenciaMin = (temp_inter_2[i*2] - temperatura_inicial[i])
        valorMinimo = temperatura_inicial[i]
    if diferenciaMax2 < temp_inter[i*2] - temperatura_inicial[i]:
        diferenciaMax2 = temp_inter[i*2] - temperatura_inicial[i]
        valorMaximo2 = temperatura_inicial[i]
    if diferenciaMin2 > temp_inter[i*2] - temperatura_inicial[i]:
        diferenciaMin2 = (temp_inter[i*2] - temperatura_inicial[i])
        valorMinimo2 = temperatura_inicial[i]

validacion = math.sqrt((validacion/datos_eliminar_num))
erroMaximo = (diferenciaMax/valorMaximo)*100
erroMinimo = abs((diferenciaMin/valorMinimo)*100)
validacion2 = math.sqrt((validacion2/datos_eliminar_num))
erroMaximo2 = (diferenciaMax2/valorMaximo2)*100
erroMinimo2 = abs((diferenciaMin2/valorMinimo2)*100)

# impresion del resultado del error
print("valores de la cuadratica")
print("el valor de error cuadratico medio es de: {:.2f}".format(validacion))
print("el valor de error maximo es de: {:.2f} %".format(erroMaximo))
print("el valor de error minimo es de: {:.2f} %".format(erroMinimo))
print("valores de la linal")
print("el valor de error cuadratico medio es de: {:.2f}".format(validacion2))
print("el valor de error maximo es de: {:.2f} %".format(erroMaximo2))
print("el valor de error minimo es de: {:.2f} %".format(erroMinimo2))

# impresion de los datos ya calculados
imprimir_resultados()
imprimir_estacion_cercaan()
