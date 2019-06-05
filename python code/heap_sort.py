# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:36:46 2019

@author: Andrew
"""

import math

class min_Heap:
    
    def __init__(self):
        self.array = []
        
    def insert(self, val):
        if (len(self.array)==0):
            self.array.append(val)
        else:
            self.array.append(val)
            i = len(self.array)
            while(i != 1):
                if(self.array[i-1] < self.array[math.floor(i/2)-1]):
                    self.array[i-1], self.array[math.floor(i/2)-1] = self.array[math.floor(i/2)-1], self.array[i-1]
                    i = math.floor(i/2)
                else:
                    break
    
    def remove(self):
        if (len(self.array)==0):
            print('the heap is currently empty')
        else:
            removed_value = self.array[0]
            self.array[0] = self.array[len(self.array)-1]
            self.array = self.array[0:len(self.array)-1]
            i=1
            while(i*2 <= len(self.array)):
                if(i*2==len(self.array)):
                    if(self.array[i-1]>self.array[(i*2)-1]):
                        self.array[i-1], self.array[(i*2)-1] = self.array[(i*2)-1], self.array[i-1]
                    else:
                        break
                else:
                    if(self.array[i-1]>self.array[(i*2)-1] or self.array[i-1]>self.array[(i*2)]):
                        if(self.array[(i*2)-1]<=self.array[(i*2)]):
                            self.array[i-1], self.array[(i*2)-1] = self.array[(i*2)-1], self.array[i-1]
                            i = i*2
                        else:
                            self.array[i-1], self.array[(i*2)] = self.array[(i*2)], self.array[i-1]
                            i = (i*2)+1
                    else:
                        break
            return(removed_value)
            


###############
## Heap Sort ##
###############
X_test = [2, 5, 3, 0, -1, 5, 2.4, -65, -2.5, 0, 10]
X_sorted = []
Heap_array = min_Heap()

for i in range(0,len(X_test)):
    Heap_array.insert(X_test[i])
    
for i in range(0,len(Heap_array.array)):
    X_sorted.append(Heap_array.remove())

X_sorted

    


             




