#https://leetcode.com/problems/binary-tree-paths/?envType=problem-list-v2&envId=tree
#Code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def dfs(node, path, paths):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path, paths)
                    dfs(node.right, path, paths)
        
        paths = []
        dfs(root, "", paths)
        return paths
