#https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=problem-list-v2&envId=matrix
#Code:
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_in_rows = {min(row) for row in matrix}
        max_in_columns = {max(column) for column in zip(*matrix)}
        return list(min_in_rows & max_in_columns)
