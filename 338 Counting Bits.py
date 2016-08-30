class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ## recursive like fibonacci sequence
        init  = [0]
        while len(init)<=num:
            for i in range(len(init)):
                init += [init[i]+1]
        return init[:num+1]
             
