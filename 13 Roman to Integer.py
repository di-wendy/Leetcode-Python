class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'M':[0,1000],"D":[1,500],'C':[2,100],'L':[3,50],'X':[4,10],'V':[5,5],'I':[6,1]}
        sequence = ['M',"D",'C','L','X','V','I']
        sum =0
        
        def convert(x):
            if x<0:
                return 0
            else:
                return x
        
        for i in range(len(s)):
            s_num = dic[s[i]][0] #Letter's index number
            if s[i]=='M':
                sum += dic[s[i]][1]
            elif (sequence[convert((s_num-2))]not in s[i:] and sequence[(s_num-1)]not in s[i:]):
                sum += dic[s[i]][1]
            else:
                sum -= dic[s[i]][1]
        return sum
