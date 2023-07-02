from NumMethPy import zeros
import math

def f1(x):
    return x**3 -2*x +1
print(zeros.bissection(f1, -10, 10, e =0.001 ))

def f2(x):
    return math.log10(x)+2
print(zeros.fixedPoint(f2, 2, 10))

def f3(x):
    return x**2 -1
print(zeros.Newton(f3, 2, 10))