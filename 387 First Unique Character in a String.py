class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occured = []
        repeated = []
        
        for l in s:
            if l in occured:
                repeated.append(l)
                index = occured.index(l)
                occured.pop(index)
            elif l not in repeated:
                occured.append(l)
        if occured == []:
            return -1
        else:
            return s.index(occured[0])
