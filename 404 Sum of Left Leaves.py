# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        global sum1
        sum1 = 0
        
        def take_sum(node):
            global sum1
            if node!= None:
                if node.left != None and node.right != None:
                    if node.left.left == None:
                        sum1 += node.left.val
                    return take_sum(node.right),take_sum(node.left)
                if node.left == None and node.right != None:
                    return take_sum(node.right)
                if node.left != None and node.right == None:
                    if node.left.left == None:
                        sum1 += node.left.val
                    return take_sum(node.left)
                if node.left == None and node.right == None:
                    return
            else:
                return

        take_sum(root)
        
        return sum1
