#https://leetcode.com/problems/intersection-of-two-arrays/?envType=problem-list-v2&envId=binary-search
#code:
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        element_count = {}
        for num in nums1:
            element_count[num] = 1  
        result = []
        for num in nums2:
            if num in element_count:
                result.append(num)
                del element_count[num]  
        return result
        
