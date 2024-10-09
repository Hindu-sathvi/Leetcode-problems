#https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=tree
#Code:
class Solution(object):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val  
            self.left = left
            self.right = right

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)  
            current = current.right

        return result
root = Solution.TreeNode(1)
root.right = Solution.TreeNode(2)
root.right.left = Solution.TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(root)) 
root2 = Solution.TreeNode(1)
root2.left = Solution.TreeNode(2)
root2.right = Solution.TreeNode(3)
root2.left.left = Solution.TreeNode(4)
root2.left.right = Solution.TreeNode(5)
root2.right.right = Solution.TreeNode(8)
root2.right.right.left = Solution.TreeNode(6)
root2.right.right.right = Solution.TreeNode(7)
root2.right.right.right.right = Solution.TreeNode(9)

print(sol.inorderTraversal(root2))
