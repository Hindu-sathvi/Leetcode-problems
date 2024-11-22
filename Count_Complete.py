#https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=problem-list-v2&envId=binary-tree
#Code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = compute_height(root.left)
        right_height = compute_height(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
