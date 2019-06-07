# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:59:42 2019

@author: Andrew
"""
import math

def Karatsuba_mult(X, Y):
        
    x_s = str(X)
    n = len(x_s)
    y_s = str(Y)
    m = len(y_s)
    
    if(n==1 or m==1):
        return(X*Y)
    else:
        A = int(x_s[0:math.floor(n/2)])        
        B = int(x_s[math.floor(n/2):n])
        C = int(y_s[0:math.floor(m/2)])        
        D = int(y_s[math.floor(m/2):m])

        AC = Karatsuba_mult(A,C)
        AD = Karatsuba_mult(A,D)
        BC = Karatsuba_mult(B,C)
        BD = Karatsuba_mult(B,D)
    
        X_times_Y = (10**(math.ceil(n/2)+math.ceil(m/2))*AC) + 10**(math.ceil(n/2))*AD + 10**(math.ceil(m/2))*BC + BD
                          
        return(X_times_Y)
        
####################
####################
X = 12345
Y = 67899
Karatsuba_mult(X, Y)