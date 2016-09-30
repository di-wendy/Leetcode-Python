class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people = sorted(people,key = lambda (h,k):(-h,k))

            
        l = len(people)
        result = []
            
        for i in range(l):
            if people[i][1]<i:
                result.insert(people[i][1],people[i])
            else:
                result.append(people[i])

        return result
                    
