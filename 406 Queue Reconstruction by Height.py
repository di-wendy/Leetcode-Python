class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def mycmp(a,b):
            if a[0] > b[0]:
                return -1
            elif a[0] == b[0]:
                if a[1] >= b[1]:
                    return 1
                if a[1] < b[1]:
                    return -1
            elif a[0] < b[0]:
                return 1
            
        people.sort(cmp = mycmp)
            
        l = len(people)
        result = []
            
        for i in range(l):
            if people[i][1]<i:
                result.insert(people[i][1],people[i])
            else:
                result.append(people[i])

        return result
