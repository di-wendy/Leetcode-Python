class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #container 1, unique numbers
        unique=[]
        #container 2, occurance
        occurs=[]
        
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
                occurs.append(1)
            else:
                occurs[unique.index(nums[i])]=occurs[unique.index(nums[i])]+1
        
        half=len(nums)/2.0
        #print unique, occurs,half
        for j in range(len(occurs)):
            if occurs[j]>=half:
                return unique[j]
