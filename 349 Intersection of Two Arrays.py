class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #built dict1 to hold numbers in array 1
        #result to hold result
        #array2 is as filter
        
        dict1 = {}
        result = []
        
        for i in range(len(nums1)):
            if nums1[i] not in dict1:
                dict1[nums1[i]]=1
        
        for i in range(len(nums2)):
            if nums2[i] in dict1:
                if dict1[nums2[i]]!=0:
                    result.append(nums2[i])
                    dict1[nums2[i]]=0
        
        return result
