class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        global op,opt
        op = 0
        opt = []
        def judge(n,op):
            if n==1:
                opt.append(op)
                return op
            if n%2 == 0:
                op+=1
                return judge(n/2,op)
            else:
                return judge(n+1,op+1),judge(n-1,op+1)
        
        judge(n,0)
        return min(opt)
