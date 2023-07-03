# Numerical-Methods
## Introduction

This projetcos consists of a Python library including some of the most common numerical methods, based on contents of the course "Numerical Methods and Applications (MAT3121)" from Escola Politécnica da Universidade de São Paulo. **This is a work in progress and other functions are yet to be implemented.**

## Implemented Methods

### Zeros of Functions
This group of functions in the library implements methods for finding the zero of a function $f$ inside a given interval $[a,b]$.
-  **Bissection Method** - `zeros.bissection`: Takes a function `f`, the limits of the interval `a` and `b`, and optionaly the number of iterations `N` or maximum error `e`. Returns the zero of the function inside the interval, which may be not unique.
- **Fixed Point Method** - `zeros.fixedPoint`: Takes a function `f`, an initial estimative `p0`and optionaly the number of iterations `N`. Returns the fixed point of the function.
- **Newton's Method** - `zeros.Newton`: Takes a function `f`, an initial estimative `p0`and optionaly the number of iterations `N`. Returns the zero of the function to which Newton's method converge.

### Derivatives
This group of functions are used to calculate the derivative of a function $f$ at a given point $p$.
- **Central** - `derivative.central`: Takes a function `f`, a point `p` and optionaly the step size `h`. Returns the derivative at $f(p)$, using the central method with step `h`.
- **Forward** - `derivative.central`: Takes a function `f`, a point `p` and optionaly the step size `h`. Returns the derivative at $f(p)$, using the forward method with step `h`.
- **Backward** - `derivative.central`: Takes a function `f`, a point `p` and optionaly the step size `h`. Returns the derivative at $f(p)$, using the backward method with step `h`.

### Integration
This group of functions are used to calculate the integral of a function $f$ in the interval $[a,b]$.
- **Trapezoidal rule** - `integration.trapezoidal`: Takes a function `f`, two points `a` and `b`, and a number of divisions `N`in the interval. Returns the numerical value of the integral.
- **Simpson's rule** - `integration.Simpson`: Takes a function `f`, two points `a` and `b`, and a number of divisions `N`in the interval. Returns the numerical value of the integral.

## Usage
This library is not inteded to be published at PyPI.
If you want to use or try it on your machine:
1. Install Git on your machine, via https://git-scm.com/downloads.
2. Clone this repository to your machine. (more on how to do this [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)).
3. Locate the file `NumMethPy-0.1.0-py3-none-any.whl` insider `dist`folder.
4. Run `pip install your-path-to/NumMethPy-0.1.0-py3-none-any.whl` to install library.
5. Use it on your programs via `import NumMethPy`.
