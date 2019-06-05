# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 04:02:38 2019

@author: Andrew
"""

def Two_sum(X, target):
    already_seen = {}
    for i in range(0,len(X)):
        if(X[i] in already_seen.keys()):
            print("The numbers " + str(X[i]) + " and " + str(already_seen[X[i]]) + " sum to " + str(target))
        else:
            difference = target - X[i]
            already_seen[difference] = X[i]



X_test_1 = [1, 2, 2, 3, 3, 6, 8, 10]
Two_sum(X_test_1, target=9)