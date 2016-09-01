class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1 or 0:
            return False
        
        dic = {"(":")","[":"]","{":"}"}
            
        stack = [s[0]]
        stack_len = 1
        
        for i in range(1,len(s)):
            if stack_len!=0 and stack[stack_len-1] in dic and s[i] == dic[stack[stack_len-1]]:
                stack.pop()
                stack_len -=1
            else:
                stack.append(s[i])
                stack_len +=1
        
        if not stack_len:
            return True
        else:
            return False
