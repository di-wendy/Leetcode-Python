# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:39:17 2016

@author: Dwang
"""

from itertools import permutations
import numpy


#to_test = ['12345', '12354', '12435'...


array1 = [0,1,1,0]
array2 = [2,1,1,5]

def decode(array1,array2):
    
    mat_len = len(array2)
    mat = ""    
    
    for i in range(mat_len):
        mat += str(array2[i])
    
    permut = list(permutations(mat)) #穷举出list,然后test,为简单可以remove duplicates
    length = len(permut[0])
    
    to_test = []
    str_num = ""
    for a in permut:
        for i in range(length):
            str_num += a[i]
        to_test.append(str_num)
        str_num = ""
    
    k = 0
     
    #Check每一个排列组合对不对
    while (k<len(to_test)):
        result  = to_test[k]
        check = True
        for i in range(0,len(array1)):
            count = 0
            for j in range(0,max(1,i)):
                if result[j]<result[i]:
                    count += 1
            if count != array1[i]:
                check = False
        if check == True:
            return result
        k+=1

print decode(array1,array2)
