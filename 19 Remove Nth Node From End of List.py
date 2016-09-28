# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        global l
        l = 0
        
        def count(head):
            global l
            if head == None:
                return
            else:
                l +=1
                return count(head.next)
                
        count(head)
        index = l - n
        
        if index == 0:
            head = head.next
            return head
        
        num = 0
        p = head
        
        while(num < index-1):
            p = p.next
            num += 1
        
        if p.next !=None:
            if p.next.next != None:
                p.next = p.next.next
            else:
                p.next = None
        
        return head
