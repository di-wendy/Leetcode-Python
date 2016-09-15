# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        global_list = []
        
        if root == None:
            return 0
        
        def cal(num1,num2):
            return num1*10+num2
        
        def carry(root,valsum):
            valsum = cal(valsum,root.val)
            if root.left == None and root.right == None:
                global_list.append(valsum)
                return None
            if root.left !=None and root.right !=None:
                return carry(root.left, valsum),carry(root.right,valsum)
            elif root.left ==None:
                return carry(root.right,valsum)
            else:
                return carry(root.left,valsum)
        
        valsum = 0
        carry(root,valsum)
        
        return sum(global_list)
