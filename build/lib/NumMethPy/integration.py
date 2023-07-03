def trapezoidal(f:"function", a:float, b:float, N:int = 1) -> float:
    """Calculates the integral of a function f inside the interval [a,b], 
    using the trapezoidal rule.
    Use N divisions in the interval, 1 by default.
    
    :param f: function to be integrated
    :param a: lower limit of integration interval
    :param b: higher limit of integration  interval
    :param N: number of divisions
    :return: integral value"""


    h = (b-a)/N
    I = 0
    for i in range(0, N):
        I += (h/2)* (f(a + i*h) + f(a + (i+1)*h))
    return I


def Simpson(f, a, b, N=1):
    """Calculates the integral of a function f inside the interval [a,b], 
    using Simpson's rule.
    Use N divisions in the interval, 1 by default.
    
    :param f: function to be integrated
    :param a: lower limit of integration interval
    :param b: higher limit of integration  interval
    :param N: number of divisions
    :return: integral value"""

    I = 0
    h = (b-a)/(2*N)
    for i in range(0, N):
        I += (h/3)*(f(a + 2*h*i) + 4*f(a + 2*h*i + h) + f(a + 2*h*i + 2*h))
    return I