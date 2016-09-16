class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1 or nums[1]<nums[0]:
            return 0
            
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        
        if len(nums)==2:
            return 1
        
        grad_left = []
        grad_right = []
        
        for i in range(1,len(nums)-1):
            if(nums[i]-nums[i-1])>0 and (nums[i]-nums[i+1])>0:
                return i

        return 0
        
