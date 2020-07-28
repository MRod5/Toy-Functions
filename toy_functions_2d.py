"""
Toy functions for testing optimization algorithms.

Includes famous functions such as:
    + Otis peaks
    + Goldstein-Price
    + Easom's
    + Six-hump camel back
    + Branin's rcos
    
Also includes:
    + eggcup
    + toboggan
    + mesa
    + corrugada
    + testf4
    

MRodriguez - 2020
"""

import numpy as np 

## Otis Peaks:
def otis_peaks(x1, x2):
    """
    Función para tests 2D: Otis Peaks.
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 1
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-5,5], [-5,5]
    
    MRod
    """

    f_value = -10*x1**2 + 10*x2**2 + 4*np.sin(x1*x2) - 2*x1 +x1**4
    
    return f_value
    

## Goldstein-Price
def goldstein(x1, x2):
    """
    Función para tests 2D: Goldstein-Price.
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-5,5], [-5,5]
        Mínimo de la función en (x1,x2)=(0,-1); f(x1, x2)=3
    
    MRod
    """

    f_value = ( (1+((x1+1+x2)**2)*(19-14*x1+3*x1**2-14*x2+ 
               6*x1*x2+3*x2**2)) * (30+((2*x1-3*x2)**2)*(18-32*x1
               +12*x1**2+48*x2-36*x1*x2+27*x2**2)) )

    return f_value
    
    
## Easom
def easom(x1, x2):
    """
    Función para tests 2D: Easom's
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-5,5], [-5,5]
        Mínimo de la función en (x1,x2)=(pi,pi); f(x1, x2)=-1
    
    MRod

    """
    
    f_value =-np.cos(x1)*np.cos(x2)*np.exp(-((x1-np.pi)**2+(x2-np.pi)**2))
    
    return f_value

    
## Six-hump camel back
def sixhump(x1, x2):
    """
    Función para tests 2D: Six-hump camel back
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-2,2], [-2,2]
        Mínimo de la función en (x1,x2)=(0.0898,-0.7126); f(x1, x2)=-1.0316
    
    MRod

    """

    f_value = (4-2.1*x1**2 + x1**4/3)*x1**2 + x1*x2 + (-4 + 4*x2**2)*x2**2

    return f_value


## Branin's rcos
def branin(x1, x2):
    """
    Función para tests 2D: Branin rcos
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-5,10], [0,15]
        Mínimo de la función en (x1,x2)=(pi, 12.275); f(x1, x2)=0.397887
        Mínimo de la función en (x1,x2)=(pi, 2.275)
        Mínimo de la función en (x1,x2)=(9.42478, 2.475)
    
    MRod

    """

    a=1
    b=5.1/(4*np.pi**2)
    c=5/np.pi
    d=6
    e=10
    f=1/(8*np.pi)

    f_value =a*(x2 - b*x1**2 + c*x1 - d)**2 + e*(1-f)*np.cos(x1) + e

    return f_value
    

## F5: huevera
def eggcup(x1, x2):
    """
    Función para tests 2D: Huevera
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-4, 4], [-4, 4]
    
    MRod - Feb 2012
    """
    
    f_value = 10*((np.cos(x1))**2+(np.sin(x2))**2);
    return f_value


## F1: Tobogan
def toboggan(x1, x2):
    """
    Función para tests 2D: Tobogan
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-4, 4], [-4, 4]
    
    MRod - Feb 2012
    """
    
    f_value = (np.sin(x1)+np.cos(x2))*np.exp(-((x1)**2+(x2)**2))*x1
    return f_value


## F2: Meseta
def mesa(x1,x2):
    """
    Función para tests 2D: Meseta
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-7, 7], [-7, 7]
    
    MRod - Feb 2012
    """

    f_value = (x1+x2)**2*((np.cos(x1))**2+(np.sin(x2))**2)
    return f_value


## F3: corrugada
def corrugada(x1,x2):
    """
    Función para tests 2D: Corrugada
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo [-7, 7], [-7, 7]
    
    MRod - Feb 2012
    """

    f_value = 100*np.cos(x1*5)*np.exp(-x2*2)*x1**2
    return f_value


## F4
def testf4(x1,x2):
    """
    Función para tests 2D: 
    
    Inputs: 
        x1: array_like. Variable independiente 1
        x2: array_like. Variable independiente 2
        
    Returns:
        f_value: array_like. valores de la función para cada posición de x1, x2
        
    Notes:
        Funciona bien en intervalo 
    
    MRod - Feb 2012
    """

    f_value = np.cos(x1)*x2;
    return f_value

