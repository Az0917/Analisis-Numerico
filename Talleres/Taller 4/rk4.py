import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    #return x**2-3*y
    return x**(3*x)-40*y

# (f(x,y),a(punto inicial),b(punto final),y0(condicion inicial),h(paso)
def rk4(f,a,b,y0,h):
    x = np.arange(a,b+h,h)
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        k1 = f(x[i], y[i])
        k2 = f(x[i]+h/2, y[i]+k1*h/2)
        k3 = f(x[i]+h/2, y[i]+k2*h/2)
        k4 = f(x[i]+h, y[i]+k3*h)
        y[i+1] = y[i]+(h/6)*(k1+2*k2+2*k3+k4)
    error(n, int(h))
    plt.plot(x, y)
    plt.show()

def digitosCont(n):
    cant = 1
    while n > 9:
        n = n / 10
        cant = cant + 1
    return cant

def digitos(n):
    return list(map(int, str(n)))

def error(n, cap):
    expo = digitosCont(n)
    notacion = int(n * (pow(10, expo - 1)))
    arreglo = digitos(notacion)

    truncamiento = 0
    for i in range(cap, len(arreglo)):
        truncamiento = (truncamiento * 10) + arreglo[i]

    valor = truncamiento / 10
    error = expo - cap

    print("El error de truncamiento es :", valor, "x10^", error)


#rk4(f,1,2,10,0.4)
#rk4(f,1,2,10,0.01)
rk4(f,1,2,10,1.55)


