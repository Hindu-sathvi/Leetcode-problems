#https://leetcode.com/problems/sum-of-left-leaves/description/?envType=problem-list-v2&envId=tree
#Code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        if root is None:
            return 0
        
        total = 0
        if root.left and isLeaf(root.left):
            total += root.left.val
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total