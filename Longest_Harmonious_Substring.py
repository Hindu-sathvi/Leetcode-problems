#https://leetcode.com/problems/longest-harmonious-subsequence/?envType=problem-list-v2&envId=sliding-window
#Code:
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
  
        num_counts = Counter(nums)  
        max_length = 0  
    
        for num in num_counts:
            if num + 1 in num_counts:  
                current_length = num_counts[num] + num_counts[num + 1]
                max_length = max(max_length, current_length) 
            
        return max_length