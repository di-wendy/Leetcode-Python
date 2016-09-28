# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        q1 = head
        
        while(q1 !=None and q1.next != None):
            q1 = q1.next
            if q1.val != p1.val:
                p1 = p1.next
            while(q1!=None and q1.val == p1.val):
                q1 = q1.next
            p1.next = q1

        return head
