class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 #pointer
        dict = {} #Dictionary
        sums = 0
        
        while i<len(nums):
            if nums[i] not in dict:
                dict[nums[i]]=1
                i+=1
            else:
                nums.pop(i)
        
        return len(nums)
