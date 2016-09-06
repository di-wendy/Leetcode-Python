class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
            
        def invertsub(root):
            if root.left == None and root.right == None:
                return root
            elif root.left == None:
                root.left = root.right
                root.right = None
                return invertsub(root.left)
            elif root.right == None:
                root.right = root.left
                root.left = None
                return invertsub(root.right)
            else:
                root.left,root.right = root.right, root.left
                return invertsub(root.left),invertsub(root.right)
                
        invertsub(root)
        return root
