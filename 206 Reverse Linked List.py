class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.next == None:
            return head
            
        if head.next.next == None:
            head.next.next = head
            h = head.next
            head.next = None
            return h
        
        o = head
        p = head.next
        q = head.next.next
        
        o.next = None
        while q != None:
            p.next = o
            o = p
            p = q
            q = q.next
            
        p.next = o
        return p
