#https://leetcode.com/problems/two-sum/
#Two_sum:
#code:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            k=i+1
            for j in range(k,len(nums)):
               if(nums[i]+nums[j]==target):
                      return [i, j] 
        return []
#Implementing using Hashmap
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Implementing using hashmap
        prevmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevmap:
                return[prevmap[diff],i]
            prevmap[n]=i
        return

        
