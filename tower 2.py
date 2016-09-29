# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:54:07 2016

@author: Dwang

Given:
Plaintext to encrypt
A key defined by a square matrix

加密过程：
1. 首先将所有的转换成大写
2. 去掉字符 Hi!there  -> HITHERE
3. 搜索矩阵，将#换成字母，从左到右换
4. 读取矩阵，从上往下读，读出以后，输出五字母一组
5. 如果矩阵用完了，再来一遍

"""

import numpy as np

inp1 = "Hi, There!!!"
inp2 = [['#','&','#'],['&','#','#'],['#','#','#']]

def encode(inp1,inp2):
    en_matrix = np.copy(inp2)  #储备矩阵 deepcopy
    
    temp_list = []
    row = 0
    column = 0
    width = len(inp2[0])
    height = len(inp2)    
    
    #Encode
    for letter in inp1:
        if letter.isalpha():
            while(inp2[row][column]!='#'):
                column += 1
                if column >= width:
                    column = 0
                    row += 1
                if row >= height:
                    temp_list.append(inp2)
                    inp2 = np.copy(en_matrix)
                    row = 0
                    column = 0    #目的为循环Search到井的column和row
                    
            inp2[row][column] = letter
            column += 1
            if column >= width:
                column = 0
                row += 1
            if row >= height:
                temp_list.append(inp2)
                inp2 = np.copy(en_matrix)
                row = 0
                column = 0
    
    temp_list.append(inp2)
    
    #Decode
    result = ""
    k = 0
    
    while(k<len(temp_list)):
        to_decode = temp_list[k]
        for i in range(width):
            for j in range(height):
                if to_decode[j][i].isalpha():
                    result += to_decode[j][i]
        k+=1
    
    #Upper Case, insert space
    result = result.upper()
    
    def encrypt(string, length):
        return ' '.join(string[i:i+length] for i in xrange(0,len(string),length))
    
    result = encrypt(result,5)
        
    
    return result



