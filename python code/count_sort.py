# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:15:27 2019

@author: Andrew
"""


def count_sort(X, max_num):
    
    X_compressed = (max_num+1)*[0]
    
    for i in range(0, len(X)):
        X_compressed[X[i]] = X_compressed[X[i]]+1
        
    X_sorted = []
    for i in range(0, len(X_compressed)):
        if(X_compressed[i] > 0):
            X_sorted = X_sorted + X_compressed[i]*[i]
    
    return(X_sorted)
            

######################
######################
X_test_1 = [3,6,1,2,2,1,0,0,9,5,34,1,23,34,34,1,0]
max_num = 34
count_sort(X_test_1, max_num)

                    
            
            
            
            
            
            
        
        

