#code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def traverse(node,result):
            if(node):
                traverse(node.left,result)
                result.append(node.val)
                traverse(node.right,result)
        result1=[]
        result2=[]
        traverse(p,result1)
        traverse(q,result2)
        return result1 == result2 
