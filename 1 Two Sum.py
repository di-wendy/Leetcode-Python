class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Hashmap
        pmap = {}
        
        for i in range(len(nums)):
            if (target-nums[i]) in pmap:
                return [pmap[target-nums[i]],i]
                break
            else:
                pmap[nums[i]]=i
