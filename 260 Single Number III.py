class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = len(nums)-1

        while (i>=0):
            if (nums[i]==nums[i-1]):
                nums.pop(i)
                nums.pop(i-1)
                i -= 2
            else:
                i -=1
        
        return nums
