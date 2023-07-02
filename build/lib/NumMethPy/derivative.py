def central(f:"function", p:float, h:float =0.01) -> float:
    """Calculates the central derivative of function f at point p. 
    Uses a step of h, 0.01 by default.
    
    :param f: function which derivative is to be found
    :param p: point to calculate derivative
    :param h: step used in calculation
    :return: fixed point of the function"""

    return (f(p+h/2) - f(p-h/2))/(h)


def forward(f:"function", p:float, h:float =0.01) -> float:
    """Calculates the forward derivative of function f at point p. 
    Uses a step of h, 0.01 by default.
    
    :param f: function which derivative is to be found
    :param p: point to calculate derivative
    :param h: step used in calculation
    :return: fixed point of the function"""

    return (f(p+h) - f(p))/(h)


def backward(f:"function", p:float, h:float =0.01) -> float:
    """Calculates the backward derivative of function f at point p. 
    Uses a step of h, 0.01 by default.
    
    :param f: function which derivative is to be found
    :param p: point to calculate derivative
    :param h: step used in calculation
    :return: fixed point of the function"""

    return (f(p) - f(p-h))/(h)