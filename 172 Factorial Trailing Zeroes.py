class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        while n:
            n /=5
            a +=n
        return a
