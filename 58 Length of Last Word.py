class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.count(" ")==len(s):
            return 0
        result = s.split()
        
        return len(result[len(result)-1])
