# -*- coding: utf-8 -*-
"""

MRodriguez - 2020    
"""
import numpy as np
import toy_functions_2d as test_fun
from matplotlib import pyplot as plt


function_switch = {
                   'toboggan': test_fun.toboggan,
                   }

boundaries_switch = {
                     'toboggan': np.array([[-4,4],[-4,4]]),
                     }


                   
class FitnessTester():
    def __init__(self, testfunction):
        if testfunction in function_switch:
            self.qfun = function_switch[testfunction]
            self.x1boundary = boundaries_switch[testfunction][0]
            self.x2boundary = boundaries_switch[testfunction][1]
        else:
            print('Function name not recognized: {}'.format(testfunction))
                

        self.testfunction = testfunction
        
        return None
        
        
    def quality_function(self,x1, x2):
        out_of_bounds = False
        if ((np.any(x1<self.x1boundary[0]) or np.any(x1>self.x1boundary[1])) or
            (np.any(x2<self.x2boundary[0]) or np.any(x2>self.x2boundary[1]))):
            out_of_bounds = True 
        
        if out_of_bounds:
            print('Independent variables out of bounds: [{},{}];[{},{}]'.format(
                      self.x1boundary[0], self.x1boundary[1], self.x2boundary[0], self.x2boundary[1]))
            print('x1={}; x2={}'.format(x1, x2))
            return None
        else:
            ff = self.qfun(x1, x2)
            return ff
                

    def quality_function_plotter(self):
        ## Vector para inputs:
        npuntos = 61
        x1 = np.linspace(self.x1boundary[0], self.x1boundary[1], npuntos)
        x2 = np.linspace(self.x2boundary[0], self.x1boundary[1], npuntos)
        
        # Malla de datos
        x1, x2 = np.meshgrid(x1, x2)
        
        ## Llamada a la función:
        funcion = self.quality_function(x1,x2)
        
        
        ## Plot de la función:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.scatter(x1, x2, funcion, c=funcion)
        
        plt.show()
        
        return None