class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []
        
        for i in xrange(0,numRows):
            result.append([1]*(i+1))
            for j in xrange(0,i+1):
                if j!=0 and j!=i:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result
