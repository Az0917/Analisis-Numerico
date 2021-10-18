from scipy import interpolate

# definicion de las variables de la escala de gravemen
base_imponible = [4410000, 4830000, 5250000, 5670000]
cuota_integral = [1165978, 1329190, 1501474, 1682830]
tipo = [38.86, 41.02, 43.18, 0]

# definicon de variables de la interpolacion lineal
interpolacion_base_cuota = interpolate.interp1d(base_imponible, cuota_integral)
interpolacion_cuota_tipo = interpolate.interp1d(cuota_integral, tipo)


valor_base = input("ingrese por favor el valor de su base: ")
valor_cuota = interpolacion_base_cuota(valor_base)
print("Usted tiene una cuota integra con un valor de: ",
      valor_cuota)

print("El valor del tipo es de: {:.2f} %".format(
    interpolacion_cuota_tipo(valor_cuota)))
