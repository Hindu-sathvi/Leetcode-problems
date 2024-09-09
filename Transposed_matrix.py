#https://leetcode.com/problems/transpose-matrix/description/?envType=problem-list-v2&envId=matrix
#code:
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        transposed_matrix = []
        for i in range(cols):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            transposed_matrix.append(new_row)

        return transposed_matrix
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
print(solution.transpose(matrix1))
