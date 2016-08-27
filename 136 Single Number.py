class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #The concept of xor
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
            
        
        return result
