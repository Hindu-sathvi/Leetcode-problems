#https://leetcode.com/problems/minimum-absolute-difference/?envType=problem-list-v2&envId=sorting
#Code:
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        result = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_diff = min(min_diff, diff)

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
    
        return result