#https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=problem-list-v2&envId=binary-search
#Code:
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_count = 0
        neg_count = 0
    
        for num in nums:
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1
    
        return max(pos_count, neg_count)
    #Using Binary Search
  def maximum_count(nums):
    def binary_search_first_zero(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def binary_search_first_positive(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        return left 

    neg_count = binary_search_first_zero(nums)
  
    pos_count = len(nums) - binary_search_first_positive(nums)
  
    return max(neg_count, pos_count)



