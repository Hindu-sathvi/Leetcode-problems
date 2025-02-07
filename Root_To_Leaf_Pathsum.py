#https://leetcode.com/problems/path-sum/
#Code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
  
        return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
        
        
