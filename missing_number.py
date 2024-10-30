#https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=binary-search
#code1:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
#code2:
# using binary search
class Solution:
    def missingNumber(nums):
        nums.sort() 
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
       
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
  
    return left

