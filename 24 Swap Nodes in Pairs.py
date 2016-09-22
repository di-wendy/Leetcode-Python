# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        mark = head.next
        
        while (head.next != None):
                pin = head.next.next  #store pointer at position 3
                np = head.next
                np.next = head
                head.next = pin
                head = pin
