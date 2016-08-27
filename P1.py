# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:06:11 2016

@author: diwang
"""

def twoSum(nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num2=[ ]      
        
        for j in range(0,len(nums)):
            num2.append(nums[j])

        for i in range(0,len(nums)):
            item = target-nums[i]
            last = len(nums)-1
            found = False
            first = i+1
            while first<=last and not found:
                midpoint = (first + last)/2
                if num2[midpoint] == item:
                    found = True
                else:
                    if item < num2[midpoint]:
                        last = midpoint-1
                    else:
                        first = midpoint+1
    	       
        variable=[i,midpoint]
        return variable