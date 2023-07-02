import math
from NumMethPy import derivative

def bissection(f:"function", a:float, b:float, N:int = 10, e:float = 0 ) -> float:
    """Calculates a zero of the function f between the interval [a,b]. 
    Please notice that the zero found may be not unique.
    If 'e' given, the algorythm iterates for N times, enough to achieve an error less than 'e'.
    Otherwise, it iterates for given N times, 10 by default.
    
    :param f: function which zero is to be found
    :param a: lower limit of search interval
    :param b: higher limit of search interval
    :param N: number of iterations wanted
    :param e: maximum error wanted (priority over N)
    :return: zero of the function contained in [a,b], not necessarily unique."""

    try:
        f(a)*f(b)>0
    except:
        print("Bissection method does not applies since f(a)*f(b)>0.")
        return None
    
    z = (a+b)/2

    if e != 0:
        N = round(math.log2((b-a)/(2*e))+1)

    
    n = 0
    while n < N:
        if (f(a)*f(z) > 0):
            a = z
        elif (f(a)*f(z) < 0):
            b = z
        else:
            return z
        z = (a+b)/2
        n+=1
    return z


def fixedPoint(f:"function", p0:float, N:int=10) -> float:
    """Calculates the fixed point of f given an initial estimative p0. 
    It iterates for given N times, 10 by default.
    
    :param f: function which fixed is to be found
    :param p0: initial estimative
    :param N: number of iterations
    :return: fixed point of the function"""
    
    if abs(derivative.central(f, p0, 0.01)) >1:
        print("The absolute derivative at chosen point is greater than 1. Make sure to choose a p0 inside an interval for which the absolute of derivative of the function is always less than 1.")
        return None

    p = p0
    n = 0
    while n < N:
        p = f(p)
        n += 1
    
    if abs(f(p)-p)<abs(f(p0)-p0):
        return p
    else:
        print("Fixed point method diverged. Make sure to choose a p0 inside an interval for which the absolute of derivative of the function is always less than 1.")
        return None


def Newton(f:"function", p0:float, N:int=10) -> float:
    """Calculates the zero of a function f starting at an initial estimative p0. 
    It iterates for given N times, 10 by default.
    
    :param f: function which fixed is to be found
    :param p0: initial estimative
    :param N: number of iterations
    :return: zero of the function"""

    p = p0
    n = 0
    while n < N: 
        dfp = derivative.central(f,p,0.01)
        p = p- (f(p))/dfp
        n += 1

    if abs(f(p)) < abs(f(p0)):
        return p
    else:
        print("Newton's method diverged. Make sure to choose a p0 respecting convexity criteria.")




    
   



