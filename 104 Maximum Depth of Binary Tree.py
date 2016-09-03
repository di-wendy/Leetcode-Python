class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        length = 0
        
        if root == None:
            return 0
        
        def isroot(root,length):
            if (root.right == None and root.left == None):
                length += 1
                return length
            else:
                length +=1
                if root.left == None:
                    return isroot(root.right,length)
                if root.right == None:
                    return isroot(root.left,length)
                return max(isroot(root.left,length),isroot(root.right,length))
                
        return isroot(root,length)
