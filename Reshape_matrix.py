#https://leetcode.com/problems/reshape-the-matrix/description/?envType=problem-list-v2&envId=matrix
#code:
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Get the number of rows and columns of the original matrix
        m = len(mat)
        n = len(mat[0])

        # Check if the reshaping is possible
        if m * n != r * c:
            return mat  # Return the original matrix if reshaping is not possible

        # Flatten the original matrix in a simpler form
        flat_list = []
        for row in mat:
            for num in row:
                flat_list.append(num)

        # Create the reshaped matrix
        reshaped_matrix = []
        index = 0  # To track the position in flat_list
        for i in range(r):
            new_row = []  # Create a new row
            for j in range(c):
                new_row.append(flat_list[index])  # Append the element at the current index
                index += 1  # Move to the next element in flat_list
            reshaped_matrix.append(new_row)  # Append the row to the reshaped matrix

        return reshaped_matrix
solution = Solution()
mat1 = [[1, 2], [3, 4]]
r1, c1 = 1, 4
print(solution.matrixReshape(mat1, r1, c1)) 
