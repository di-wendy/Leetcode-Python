class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        check = True
        
        def checknode(p,q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p != None and q!=None and p.val!=q.val:
                return False
            else:
                return (checknode(p.left,q.left) and checknode(p.right,q.right))
        
        check = checknode(p,q)
        return check
