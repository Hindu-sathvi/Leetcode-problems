#https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=array
#Code:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[i]==nums[j]:
                    return True

            return False

        