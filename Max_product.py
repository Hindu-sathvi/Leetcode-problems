#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/?envType=problem-list-v2&envId=heap-priority-queue
#Code:
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)
        
