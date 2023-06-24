from NumMethPy import zeros

def f(x):
    return x**3 -2*x +1

print(zeros.bissection(f, -10, 10, e =0.001 ))