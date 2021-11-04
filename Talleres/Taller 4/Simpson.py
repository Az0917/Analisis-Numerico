import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt

def simps(f,a,b,N):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

p1=1.26145125
p2=2.97026060
p3=6.29158016
areaAcumulada = 0
s1 = simps(lambda x : 4+np.cos(x+1),0,p1,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),0,p1,100)
areaAcumulada = areaAcumulada + s1-s2

s1 = simps(lambda x : 4+np.cos(x+1),p1,p2,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),p1,p2,100)
areaAcumulada = areaAcumulada + s2-s1

s1 = simps(lambda x : 4+np.cos(x+1),p2,p3,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),p2,p3,100)
areaAcumulada = areaAcumulada + s1-s2

print("El are es de: {:0.8f}".format(areaAcumulada))
