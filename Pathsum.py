#https://leetcode.com/problems/path-sum/?envType=problem-list-v2&envId=tree
#code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
    
        if not root.left and not root.right:
            return targetSum == root.val
  
        newSum = targetSum - root.val
        left_has_sum = self.hasPathSum(root.left, newSum)
        right_has_sum = self.hasPathSum(root.right, newSum)
        return left_has_sum or right_has_sum
        
