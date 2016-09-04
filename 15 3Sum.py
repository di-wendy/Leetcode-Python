class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums.sort()
        if len(nums)<3:
            return solution
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = -(nums[i]+nums[j])
                p = j+1
                q = len(nums)-1
                while(p < q):
                    if(sum == nums[p] or sum == nums[q]):
                        solution.append([nums[i],nums[j],sum])
                        print i,j
                        break
                    elif (sum<=nums[(p+q)/2]):
                        q = (p+q)/2-1
                    else:
                        p = (p+q)/2+1
                        
        return solution
