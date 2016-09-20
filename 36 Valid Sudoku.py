class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #Check Line
        for line in board:
            dic = {}
            for l in line:
                if l != '.':
                    if l in dic:
                        return False
                    else:
                        dic[l]=1
        
        #Check col
        for col in range(len(board[0])):
            dic = {}
            for line in range(len(board)):
                if board[line][col] != '.':
                    if board[line][col] in dic:
                        return False
                    else:
                        dic[board[line][col]]=1
        
        #Check Square
        for line in range(0,9,3):
            for col in range(0,9,3):
                dic = {}
                for delta_line in range(0,3):
                    for delta_col in range(0,3):
                        if board[line+delta_line][col+delta_col] != '.':
                            if board[line+delta_line][col+delta_col] in dic:
                                return False
                            else:
                                dic[board[line+delta_line][col+delta_col]]=1
        return True
