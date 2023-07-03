from NumMethPy import zeros, integration, ode
import math
import matplotlib.pyplot as plt

def f1(x):
    return x**3 -2*x +1
print(zeros.bissection(f1, -10, 10, e =0.001 ))

def f2(x):
    return math.log10(x)+2
print(zeros.fixedPoint(f2, 2, 10))

def f3(x):
    return x**2 -1
print(zeros.Newton(f3, 2, 10))

print(integration.Simpson(f3, 0, 3, 10))
print(integration.trapezoidal(f3, 0, 3, 10))



dy1 = lambda t, y: y[1]
dy2 = lambda t, y: -y[0] - 0.5*y[1]

tempo, valores = ode.RK4([dy1, dy2],[1,0],0, 50, 0.01)
plt.plot(tempo, valores[0], linewidth=2)
plt.plot(tempo, valores[1], linewidth=1)
#plt.plot(valores[0], valores[1])
plt.xlabel("Time (s)")
plt.ylabel("y(t)")
plt.show()