class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #convert to binary int
        def convert(a):
            #type a string
            #rtype int
            sum=0
            for i in range(len(a)):
                sum += int(a[i])*2**(len(a)-1-i)
            return sum
        answer = convert(a) + convert(b)
        answer = bin(answer)
        return answer[2:]
