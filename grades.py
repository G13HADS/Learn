# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:15:17 2020

@author: tachi
"""

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

func = lambda Theta: np.sin(1/2 * Theta[0]**2 - 1/4* Theta[1] **2 +3 ) * np.cos(2*Theta[0] + 1 - np.e**Theta[1])

res=100

_X=np.linspace(-2,2,res)
_Y=np.linspace(-2,2,res)
_Z=np.zeros((res,res))

for ix,x in enumerate(_X):
    for iy,y in enumerate(_Y):
        _Z[iy,ix]= func([x,y])
        
        
Theta = np.random.rand(2) * 4 -2
plt.plot(Theta[0],Theta[1],"o",c="red")
plt.contourf(_X,_Y,_Z,100)
plt.colorbar()

_T=np.copy(Theta)
h=0.001
lr=0.001
grad = np.zeros(len(Theta))

for i in range(10000):
    for it,th in enumerate(Theta):
        _T=np.copy(Theta)
        _T[it] = _T[it] + h
        grad[it] = (func(_T) - func(Theta) )/ h
    Theta = Theta - lr*grad
    if i%100 == 0:
        plt.plot(Theta[0],Theta[1],".",c="white")


plt.plot(Theta[0],Theta[1],"o",c="purple")
plt.show()