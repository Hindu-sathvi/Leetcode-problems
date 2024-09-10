#https://leetcode.com/problems/matrix-diagonal-sum/?envType=problem-list-v2&envId=matrix
#code:
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total= 0
        
        # Sum the primary diagonal
        for i in range(n):
            total += mat[i][i]
        
        # Sum the secondary diagonal
        for i in range(n):
            total += mat[i][n - i - 1]
        
        # If the matrix has an odd size, subtract the middle element (since it's counted twice)
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        
        return total
solution = Solution()
mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(solution.diagonalSum(mat1))
