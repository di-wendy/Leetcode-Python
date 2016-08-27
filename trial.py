# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:46:23 2016

@author: diwang
"""
import math
import numpy as np

def ucdistance(x,y,x1,y1):
    d = math.sqrt((x-x1)**2+(y-y1)**2)
    return d

def madistance(x,y,x1,y1):
    d = abs(x-x1)+abs(y-y1)
    return d

q_x = 4
q_y = 2

test_point = [(1,6),(2,4),(3,7),(6,8),(7,1),(8,4)]

d_list = []

for i in range (0,6):
    distance = madistance(test_point[i][0],test_point[i][1],q_x,q_y)
    d_list.append(distance)

print d_list

d_list.sort()

print d_list

d_list2=[8,16,50.0,68]

print np.average(d_list2)
