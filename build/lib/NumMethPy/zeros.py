import math

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
    
   



