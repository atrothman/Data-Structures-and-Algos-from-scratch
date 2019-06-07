# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:38:38 2019

@author: Andrew
"""

import numpy as np

def Strassens_Matrix(X, Y):
    p = X.shape[0]
    
    if(p==2):
        return(np.dot(X, Y))
    else:
        A = X[0:int(p/2), 0:int(p/2)]
        B = X[0:int(p/2), int(p/2):p]
        C = X[int(p/2):p, 0:int(p/2)]
        D = X[int(p/2):p, int(p/2):p]
    
        E = Y[0:int(p/2), 0:int(p/2)]
        F = Y[0:int(p/2), int(p/2):p]
        G = Y[int(p/2):p, 0:int(p/2)]
        H = Y[int(p/2):p, int(p/2):p]

        P1 = Strassens_Matrix(A, (F-H))
        P2 = Strassens_Matrix((A+B), H)
        P3 = Strassens_Matrix((C+D), E)
        P4 = Strassens_Matrix(D, (G-E))
        P5 = Strassens_Matrix((A+D), (E+H))
        P6 = Strassens_Matrix((B-D), (G+H))
        P7 = Strassens_Matrix((A-C), (E+F))

        product = np.full((p, p), None)
        product[0:int(p/2), 0:int(p/2)] = P5+P4-P2+P6
        product[0:int(p/2), int(p/2):p] = P1+P2
        product[int(p/2):p, 0:int(p/2)] = P3+P4
        product[int(p/2):p, int(p/2):p] = P1-P5-P3-P7

        return(product)


np.random.seed(123456)
p=4
X = np.random.uniform(low=-5, high=5, size=p*p).reshape(p,p)
Y = np.random.uniform(low=-5, high=5, size=p*p).reshape(p,p)
product = Strassens_Matrix(X, Y)
product

np.dot(X,Y)