class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Quinary range 1-3999
        
        dic = {0:{1:'M'},1:{1:'C',5:'D'},2:{1:'X',5:'L'},3:{1:'I',5:'V'}}

        convert = [1000,100,10,1]
        roman = [num/convert[0]]
        
        #Convert to multiplication to numbers
        for i in range(1,len(convert)):
            num = num-convert[i-1]*roman[i-1]
            roman.append(num/convert[i])
        
        #Convert to roman number
        
        result = ""
        
        for i in range(len(roman)):
            value = roman[i]
            if value == 0:
                continue
            else:
                if value in range (1,4):
                    result += dic[i][1]*value
                if value ==4:
                    result += dic[i][1]+dic[i][5] #
                if value in range (5,9):
                    result += dic[i][5]+dic[i][1]*(value%5)
                if value ==9:
                    result += dic[i][1]+dic[i-1][1]
                    
        return result
