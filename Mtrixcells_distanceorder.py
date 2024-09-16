#https://leetcode.com/problems/matrix-cells-in-distance-order/?envType=problem-list-v2&envId=matrix
#code:
class Solution:
    def DistanceOrder(self, rows, cols, rCenter, cCenter):
        # Create a list of all the cells in the matrix
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((r, c))

        # Define a function to calculate the Manhattan distance for a cell
        def calculate_distance(cell):
            row_distance = abs(cell[0] - rCenter)  
            col_distance = abs(cell[1] - cCenter)  
            total_distance = row_distance + col_distance  
            return total_distance

        # Sorting the cells
        cells.sort(key=calculate_distance)

        return cells
sol = Solution()
rows = 2
cols = 3
rCenter = 1
cCenter = 2
result = sol.DistanceOrder(rows, cols, rCenter, cCenter)
print(result)
