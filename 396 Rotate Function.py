class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        val = []
        i = 0
        j = 0
        sumval = sum(A)
        
        new_sum = 0
        
        while j < len(A)+i:
            new_sum += A[j%len(A)]*(j-i)
            j+=1
            
        for i in range(0,len(A)):
            new_sum += (sumval - len(A)*A[len(A)-i-1])
            val.append(new_sum)
        
        if val == []:
            return 0
        return max(val)
