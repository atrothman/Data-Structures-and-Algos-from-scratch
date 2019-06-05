# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:07:32 2019

@author: Andrew
"""

def quick_sort(X):
    
    if(len(X)==1):
        return(X)
        
    if(len(X)==2):
        if(X[0]>X[1]):
            X[0], X[1] = X[1], X[0]
        return(X)
    
    if(len(X)>2):
        pivot = X[0]
        j=1
        for i in range(1, len(X)):
            if(X[i] < pivot):
                X[i], X[j] = X[j], X[i]
                j=j+1
        
        X[0], X[j-1] = X[j-1], X[0]
        
        if(j-1==0):
            X[j:len(X)] = quick_sort(X[j:len(X)])
        else:
            if(j-1==len(X)-1):
                X[0:j-1] = quick_sort(X[0:j-1])
            else:
                X[0:j-1] = quick_sort(X[0:j-1])
                X[j:len(X)] = quick_sort(X[j:len(X)])
        
        return(X)
        
          
######################
######################
X_test_1 = [2,5,3, 0, -1,5,2.4, -65, -2.5, 0, 10]
quick_sort(X_test_1)

X_test_2 = list(range(5,-10,-1))
quick_sort(X_test_2)