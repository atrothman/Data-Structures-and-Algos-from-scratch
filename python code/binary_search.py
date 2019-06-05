# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:15:27 2019

@author: Andrew
"""
import math

def merge_sort(X):
    
    if(len(X)==1):
        return(X)
        
    if(len(X)==2):
        if(X[0]>X[1]):
            X[0], X[1] = X[1], X[0]
        return(X)
    
    if(len(X)>2):
        Left = merge_sort(X[0:len(X)//2])
        Right = merge_sort(X[len(X)//2:len(X)])
        X_sorted = len(X)*[None]
        
        L_count=0
        R_count=0
        for i in range(0, len(X_sorted)):
            if(L_count==len(Left)):
                X_sorted[i:len(X_sorted)] = Right[R_count:len(Right)]
                break
                #R_count = R_count+1
            else:
                if(R_count==len(Right)):
                    X_sorted[i:len(X_sorted)] = Left[L_count:len(Left)]
                    break
                    #L_count = L_count+1
                else:
                    if(Left[L_count] < Right[R_count]):
                        X_sorted[i] = Left[L_count]
                        L_count = L_count+1
                    else:
                        X_sorted[i] = Right[R_count]
                        R_count = R_count+1
        
        return(X_sorted)



def binary_search(X, val):
    
    if(len(X)==1):
        if(X[0]==val):
            print('the array contains the value ' + str(val))
        else:
            print('NO, the array does not contain the value ' + str(val))
    
    if(len(X)==2):
        if(X[0]==val or X[1]==val):
            print('the array contains the value ' + str(val))
        else:
            print('NO, the array does not contain the value ' + str(val))
        
    if(len(X)>2):
        current_indice = math.floor(len(X)/2)
        if(X[current_indice]==val):
            print('the array contains the value ' + str(val))
        else:
            if(X[current_indice]>val):
                binary_search(X[0:current_indice], val)
            else:
                if(X[current_indice]<val):
                    binary_search(X[(current_indice+1):len(X)], val)
           
                
######################
######################
X_test_1 = [2, 5, 3, 0, -1, 5, 2.4, -65, -2.5, 0, 10]
X_sorted = merge_sort(X_test_1)
binary_search(X_sorted, -3)


                    
            
            
            
            
            
            
        
        

