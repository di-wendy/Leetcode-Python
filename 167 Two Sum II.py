class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Use double pointers head and tail
        
        p1 = 0
        p2 = len(numbers)-1
        
        while(p1<p2):
            sum = numbers[p1]+numbers[p2]
            if (sum) == target:
                return p1+1,p2+1
            elif (sum < target):
                p1 = p1+1
            else:
                p2 = p2-1
