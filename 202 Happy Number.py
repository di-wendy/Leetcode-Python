class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Cast the number to string
        d = []
        def inner(n):
            n = str(n)
            sum = 0
            for i in range(len(n)):
                sum += int(n[i])**2
                
            if sum/10 <1:
                if sum is 1:
                    return True
                elif sum in d:
                    return False
                else:
                    d.append(sum)
            return inner(sum)
        
        result = inner(n)
        return result
