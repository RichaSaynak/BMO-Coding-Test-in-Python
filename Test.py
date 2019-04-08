# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:11:04 2019

@author: Richa Saynak
"""

import numpy as np

def eval():
    nodes = {'A':0 , 'B':1, 'C': 2, 'D': 3,'E' : 4}
    adjacencymatrix = np.zeros((len(nodes),len(nodes)))
    for i in range(9):
        s1 = input("enter nodes"+str(i)) #INPUT AB5, BC4 ,CD8, DC8, DE6, AD5, CE2, EB3, AE7
        adjacencymatrix[nodes[s1[0]],nodes[s1[1]]] = s1[2]
    print(adjacencymatrix)
    
    
    #ans for distance A-B-C , A-D, A-D-C, A-E-B-C-D , A-E-D
    
    for ind in range(9):
        s = input("enter nodes to check " +str(ind))  #INPUT ABC , AD, ADC, AEBCD, AED
        d = 0
        for i in range(len(s)-1):
            if(adjacencymatrix[nodes[s[i]],nodes[s[i+1]]]==0):
                print("No route exists")
                break
            d+= adjacencymatrix[nodes[s[i]],nodes[s[i+1]]]
        print(d)
        
        
if __name__ == "__main__":
    eval()     