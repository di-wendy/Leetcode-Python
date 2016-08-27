class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #Add one to last
        digits[len(digits)-1]=digits[len(digits)-1]+1

        #add one from backward
        for i in range(len(digits)-1,0,-1):
            if digits[i]==10:
                digits[i-1]=digits[i-1]+1
                digits[i]=0
        
        #Check the first digit
        if digits[0]==10:
            digits[0]=0
            digits = [1]+digits
        
        return digits
