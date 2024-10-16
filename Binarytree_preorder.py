#https://leetcode.com/problems/binary-tree-preorder-traversal/description/?envType=problem-list-v2&envId=stack
#code:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
  
        def traverse(node):
            if node:
                result.append(node.val)  
                traverse(node.left)       
                traverse(node.right)     

        result = []
        traverse(root)
        return result

    def preorderTraversalIterative(self, root):
    
        if not root:
            return []

        result, stack = [], [root]

        while stack:
            node = stack.pop()
            result.append(node.val) 
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

if __name__ == "__main__":
 
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    solution = Solution()
    print(solution.preorderTraversal(root1))         
    print(solution.preorderTraversalIterative(root1))

 
