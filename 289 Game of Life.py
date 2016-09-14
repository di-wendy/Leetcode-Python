class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
                
        if board[0][0]==None:
            return void
            
        #def determine()
        ori_b=[]
            
        length = len(board)
        height = len(board[0])
        
        for i in range(0,length):
              temp=[]
              for j in range(0,height):
                  temp.append(board[i][j])
                  ori_b.append(temp)
        
        for i in range(0,length):
              for j in range(0,height):
                  live = 0
                  dead = 0
                  for k in range(-1,2):
                      for h in range(-1,2):
                          if (k!=0 or h !=0) and i+k>=0 and i+k<length and j+h>=0 and j+h<height:
                              #if i==0 and j==1:
                                  #print i+k,j+h
                              if ori_b[i+k][j+h]==1:
                                  if i == 0 and j==1:
                                        print i+k,j+h
                                  live+=1
                              if ori_b[i+k][j+h]==0:
                                  dead+=1
                  #if i==0 and j==1:
                      #print live

                  if board[i][j]==1:   
                      #print live
                      if live<2:
                          board[i][j]=0
                      elif live >3:
                          board[i][j]=0
                  elif board[i][j]==0 and live == 3:
                      #print live
                      board[i][j]=1
