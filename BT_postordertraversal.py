#https://leetcode.com/problems/binary-tree-postorder-traversal/?envType=problem-list-v2&envId=stack
#code:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(node):
            if node:
                traverse(node.left)       
                traverse(node.right)
                result.append(node.val)  
        
        result = []
        traverse(root)
        return result
if __name__ == "__main__":
 
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    solution = Solution()
    print(solution.postorderTraversal(root1))    

        