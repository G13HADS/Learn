# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 05:18:01 2020

@author: tachi
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import reglin

boston = load_boston()
X = np.array(boston.data[:, 5])
X = np.array([X, boston.data[:, 0]])
#X = np.array(boston.data[:, 0])
Y= np.array(boston.target)
B=reglin.MCO(X,Y)
plt.scatter(X[0],Y,alpha=0.3)
'''
fig = plt.figure()
ax = fig.gca(projection='3d')


ax.scatter(X[0], X[1],Y, c='blue', marker='o', alpha=0.3)

ax.set_xlabel('Numero de habitaciones')
ax.set_zlabel('Precio')
ax.set_ylabel('Indice de Criminalidad')
'''
plt.plot([4,9],[B[0] + B[1]*4,B[0]+B[1]*9], c="orange")
plt.show()