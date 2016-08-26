class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #
        
        for i in range(len(nums)):
            if (nums[i]==val):
                for j in range(i+1,len(nums)):
                    if nums[j]!=val:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
        
        for i in range(len(nums)-1,-1,-1):
            if (nums[i]==val):
                nums.pop()
        
        return len(nums)
