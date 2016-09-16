class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        i = 0
        
        for num in nums:
            result^=num
            result^=i
            i+=1
        
        return result
