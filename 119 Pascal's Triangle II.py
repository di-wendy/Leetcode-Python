class Solution(object):
    def getRow(self, rowIndex):
        """
        O(k) Space
        :type rowIndex: int
        :rtype: List[int]
        """
        
        temp = []
        
        for i in xrange(0,rowIndex+1):
            temp.append(1)   #length of the result i+1
            for j in range(0,i+1):
                if j!=0 and j!=i:
                    temp[0] = temp[i]   #temp[0] store last temp[j-1] through temp[i]
                    temp[i] = temp[j]   #temp[i] store temp[j]
                    temp[j] += temp[0]
        temp[0] = 1
        temp[rowIndex] = 1
        return temp
