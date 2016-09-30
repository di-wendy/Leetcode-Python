class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        num = 0
        
        
        while(n>count):
            num += 1      #0,1,2...
            count += (10**(num-1))*9*num  #9,189
        
        
        count -= (10**(num-1))*9*num   #num is the digitnum of answer
        
        if count == 0:
            return n
        
        to_convert = (n-count)/(num)
        rem = (n-count)%(num)
        
        if rem == 0:
            digit_str = str(10**(num-1) + to_convert -1)
            return int(digit_str[len(digit_str)-1])
        else:
            digit_str = str(10**(num-1) + to_convert)
            return int(digit_str[rem-1])
