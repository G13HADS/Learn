# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 05:12:45 2020

@author: tachi
"""

import numpy as np
import scipy as sp

#Implementa la funcion de MinimosCuadraticosOrdinarios Beta = (X^T X)^-1 X^T Y
def MCO(X:np.array,Y:np.array):
    #Añadimos una fila de "1"s a X para añadir el termino independiente W0
    
    if type(X[0]) == np.ndarray:
        lenmax = len(X[0])
        X1 = np.ones(lenmax)
        for i in range(len(X)):
            X1= sp.c_[X1,X[i]]
        XT= X1.T
        Beta= np.linalg.inv(XT @ X1) @ XT @ Y
    else: 
        lenmax = len(X)
        X = np.array([np.ones(lenmax), X]).T
        XT= X.T
        Beta= np.linalg.inv(XT @ X) @ XT @ Y
    
    
    
    
    
    
    
    '''
    res= sp.stats.linregress(X,Y)
    Beta = [res.intercept,res.slope]
    '''
    return Beta
