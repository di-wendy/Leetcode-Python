class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        i = 0
        num = list(num)
        
        while(k>0  and i < len(num)-1):
            if num[i] > num[i+1]:
                num.pop(i)
                k -= 1
                i -= 1 if i>0 else 0
            else:
                i += 1
        
        z = 0
        while(z<len(num) and num[z]=="0"):
            z += 1
        
        num = num[z:]
        
        if len(num) - k <= 0:
            return "0"
        else:
            return ''.join(num[:len(num)-k])
