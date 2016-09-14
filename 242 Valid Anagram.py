class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for l in s:
            if l not in dic1:
                dic1[l]=1
            if l in dic1:
                dic1[l]+=1
                
        for l in t:
            if l not in dic2:
                dic2[l]=1
            if l in dic2:
                dic2[l]+=1
        
        if len(dic1)!=len(dic2):
			return False

        for key in dic1:
            if key not in dic2:
                return False
            if dic2[key]!=dic1[key]:
                return False
        
        return True
