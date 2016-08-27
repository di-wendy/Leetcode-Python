class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #Seperate in two piece and stitch them together
        k = k%len(nums)
        array1 = nums[len(nums)-k:]
        array2 = nums[:len(nums)-k]
            
        for i in range(k):
            nums[i]=array1[i]
            
        for j in range(k,len(nums)):
            nums[j]=array2[j-k]
