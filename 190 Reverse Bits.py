class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = str(bin(n)[2:])
        while len(digit)<32:
        	digit = '0'+digit

        digit2 = int(digit[::-1],base=2)
        return digit2
