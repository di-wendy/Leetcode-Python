class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return
        
        row = []
        column = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    column.append(j)
        
        #Deal with row
        while row:
            h = row.pop()
            for j in range(len(matrix[0])):
                matrix[h][j]=0
        
        while column:
            l = column.pop()
            for i in range(len(matrix)):
                matrix[i][l]=0
