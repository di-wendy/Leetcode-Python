class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result1 = 0
        result2 = 0
        for i in range(len(s)):
            result1 += ord(s[i])
        for i in range(len(t)):
            result2 += ord(t[i])
        return chr(result2-result1)
