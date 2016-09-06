class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
            
        p = 0
        q = 0
        while(p<len(s) and q<len(t)):
            if (s[p]==t[q]):
                p+=1
                q+=1
            else:
                q+=1
        if (p==len(s)):
            return True
        else:
            return False
