#https://leetcode.com/problems/next-greater-element-i/?envType=problem-list-v2&envId=stack&difficulty=EASY
#Code:
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)
        return [next_greater[num] for num in nums1]
        
