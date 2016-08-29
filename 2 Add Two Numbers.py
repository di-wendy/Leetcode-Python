# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Conner Cases
        if l1 == None or l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        #Initialize
        result = ListNode(-1)
        p = result
        tempten = 0
        
        while (l1 !=None and l2!=None):
            tempvalue = (l1.val+l2.val+tempten)
            p.next = ListNode(tempvalue%10)
            tempten = tempvalue/10
            p = p.next
            l1 = l1.next
            l2 = l2.next
            
        #One list to the end
        if (l1):
            p.next = l1
            p = p.next
        if (l2):
            p.next = l2
            p = p.next
        if l1 == None and l2 == None:
            if p.next == None and tempten ==1:
                    p.next = ListNode(1)
                    return result.next

        while(p.next and tempten==1):
            if(p.val+tempten)>=10:
                p.val = 0
            else:
                p.val = p.val+tempten
                tempten = 0
            p = p.next
        
        #Deal with tail
        if (tempten !=0):
            if (p.val+tempten)>=10:  #The factor will be carried to exceed the list
                p.val = (p.val+tempten)%10
                p.next = ListNode(1)
            else:
                p.val+=1
        
        return result.next
            
