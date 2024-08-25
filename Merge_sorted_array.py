#https://leetcode.com/problems/merge-sorted-array/description/
#code:
class Solution:
 def merge(self,nums1, m, nums2, n):
     final = m + n - 1
     i = m - 1
     j = n - 1
     while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[final] = nums1[i]
            i -= 1
        else:
            nums1[final] = nums2[j]
            j -= 1
        
        final -= 1
        while j >= 0:
          nums1[final] = nums2[j]
          j -= 1
          final -= 1
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0, 0]
m = 3
nums2 = [2, 3, 5, 6]
n = 4
sol.merge(nums1, m, nums2, n)
print(nums1)