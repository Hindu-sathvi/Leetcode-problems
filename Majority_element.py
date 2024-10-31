class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        majority_element=n//2
        count={}
        for i in nums:
            count[i]=count.get(i, 0) + 1
        for i in count:
            if count[i]>majority_element:
                return i