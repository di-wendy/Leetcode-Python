# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:30:34 2016

@author: Dwang
"""

inp = [[3,9],[4,18],[6,13],[22,24]]

#Dynamic Programming

def caldistance(inp):
    
    start = inp[0][0]
    end = inp[0][1]  #9
    dis = 0
    i = 1
    #Boundary Condition
    if len(inp) <= 1:
        return inp[0][1] - inp[0][0]
    
    while (1):
        new_start = inp[i][0]   #4
        new_end = inp[i][1]    #18
        if new_start > end:
            dis += (end - start)
            start = new_start
            end = new_end
            
        if new_end > end:
            end = new_end
        
        i+=1
        if i == len(inp):
            dis += (end-start)
            return dis

print caldistance(inp)
