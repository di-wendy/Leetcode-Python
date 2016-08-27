# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:17:09 2016

@author: diwang
"""

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==1:
            return True
            
        while n!=0:
            m = n%3
            if m != 0:
                break
            n = n/3
            if m ==0 and (n==1 or n==3):
                return True
            else:
                continue
        return False