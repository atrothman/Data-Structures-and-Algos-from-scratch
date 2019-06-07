# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:25:16 2019

@author: Andrew
"""

def random_contraction(G):
    num_nodes = set(list(G['node1']) + list(G['node2']))
    while(len(num_nodes)>2):
        random_edge = G['edges'][np.asscalar(np.random.randint(len(G['edges']), size=1))]  
        n1 = int(G.loc[G['edges']==random_edge, 'node1'])
        n2 = int(G.loc[G['edges']==random_edge, 'node2'])
    
        G.loc[G['node1']==n1, 'node1'] = n2
        G.loc[G['node2']==n1, 'node2'] = n2
        G.drop(G.loc[G['node1']==G['node2']].index, inplace=True)
        G.reset_index(drop=True, inplace=True)
    
        num_nodes = set(list(G['node1']) + list(G['node2']))
    
        del random_edge, n1, n2
        
    return(set(G['edges']))




import pandas as pd
import numpy as np
np.random.seed(10815657)

G = pd.DataFrame()
G['edges'] = ['a', 'b', 'c', 'd', 'e']
G['node1'] = [1, 1, 3, 3, 2]
G['node2'] = [3, 2, 2, 4, 4]
iterations = 1000
min_edges = len(G['edges'])
min_cut_D = {}
for i in range(0, iterations):
    trial = random_contraction(G.copy())
    possible_key = str(trial)
    if(len(trial)<=min_edges):
        if(len(trial)<min_edges):
            min_cut_D = {}
        min_edges = len(trial)
        if(possible_key not in min_cut_D.keys()):    
            min_cut_D[possible_key] = len(trial)
            
print(min_cut_D.keys())
        
    


    
    
    



