import numpy as np

def Euler(dyVector:list , y0Vector:list, t0:float, tf:float, h:float = 0.01) -> tuple:
    """Solves the system of ODEs given for discrete times between t0 and tf, 
    using Euler's method.
    Uses a time step of h, 0.01 by default.
    
    :param dyVector: list or np array of the functions which represent the 1st order derivatives of the functions to be calculated.
    Each function must be defined as a function of time t, and of a list y, which are the other functions.
    :param y0Vector: list of initial values for each function at t0.
    :param t0: initial time.
    :param tf: end time for calculation.
    :param h: discrete time step.
    :return: a tuple including the time vector in first position and an array in which each row contains the values for a solution. """
    
    T = [t0]
    yVector = np.transpose([np.array(y0Vector, dtype= np.float16)])
    w = yVector
    t =  t0

    while t < tf:
        for i in range(0,w.size):
            w[i,0] = w[i,0] + (dyVector[i])(t, np.squeeze(np.transpose(w)))*h
        t += h
        yVector = np.c_[yVector, w]
        T.append(t)

    return T, yVector



def RK2(dyVector:list , y0Vector:list, t0:float, tf:float, h:float = 0.01) -> tuple:
    """Solves the system of ODEs given for discrete times between t0 and tf, 
    using Runge-Kutta of 2nd order method.
    Uses a time step of h, 0.01 by default.
    
    :param dyVector: list or np array of the functions which represent the 1st order derivatives of the functions to be calculated.
    Each function must be defined as a function of time t, and of a list y, which are the other functions.
    :param y0Vector: list of initial values for each function at t0.
    :param t0: initial time.
    :param tf: end time for calculation.
    :param h: discrete time step.
    :return: a tuple including the time vector in first position and an array in which each row contains the values for a solution. """
    
    T = [t0]
    yVector = np.transpose([np.array(y0Vector, dtype= np.float16)])
    w = yVector
    t =  t0

    while t < tf:
        for i in range(0,w.size):
            w[i,0] = w[i,0] + (dyVector[i])(t+(h/2), np.squeeze(np.transpose(w)) + (h/2)*(dyVector[i])(t, np.squeeze(np.transpose(w))))*h
        t += h
        yVector = np.c_[yVector, w]
        T.append(t)

    return T, yVector

def RK4(dyVector:list , y0Vector:list, t0:float, tf:float, h:float = 0.01) -> tuple:
    """Solves the system of ODEs given for discrete times between t0 and tf, 
    using Runge-Kutta of 4th order method.
    Uses a time step of h, 0.01 by default.
    
    :param dyVector: list or np array of the functions which represent the 1st order derivatives of the functions to be calculated.
    Each function must be defined as a function of time t, and of a list y, which are the other functions.
    :param y0Vector: list of initial values for each function at t0.
    :param t0: initial time.
    :param tf: end time for calculation.
    :param h: discrete time step.
    :return: a tuple including the time vector in first position and an array in which each row contains the values for a solution. """
    
    T = [t0]
    yVector = np.transpose([np.array(y0Vector, dtype= np.float16)])
    w = yVector
    t =  t0

    while t < tf:
        for i in range(0,w.size):
            k1 = h*(dyVector[i])(t, np.squeeze(np.transpose(w)))
            k2 = h*(dyVector[i])(t + h/2, np.squeeze(np.transpose(w)) + (k1/2))
            k3 = h*(dyVector[i])(t + h/2, np.squeeze(np.transpose(w)) + (k2/2))
            k4 = h*(dyVector[i])(t + h, np.squeeze(np.transpose(w)) + (k3))
            w[i,0] = w[i,0] + (1/6)*(k1+ 2*k2 + 2*k3 + k4)
        t += h
        yVector = np.c_[yVector, w]
        T.append(t)

    return T, yVector