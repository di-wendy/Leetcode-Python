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



