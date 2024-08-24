#https://leetcode.com/problems/remove-element/
#code:
class Solution:
  def removeElement(self,nums, val):
         k = 0
    for i in range(len(nums)):
        if nums[i] != val:#If the current element is not val, it means this element should remain in the list
            nums[k] = nums[i]#If the condition in the previous line is true (i.e., nums[i] is not equal to val), this line places the value of nums[i] at the index k in the list.
            k += 1
    return k
