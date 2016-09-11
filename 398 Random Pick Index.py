class Solution(object):
    def __init__(self, nums):
            """
            
            :type nums: List[int]
            :type numsSize: int
            """
            self.nums = nums
            
    def pick(self, target):
            """
            :type target: int
            :rtype: int
            """
            indexlist = [i for i,val in enumerate(self.nums) if val==target]
            return random.choice(indexlist)
