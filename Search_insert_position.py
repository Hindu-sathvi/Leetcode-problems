class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Example usage
solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target)) 
#Binary search approach is used as they asked to search the element the binary search approach is effective
# because it efficiently narrows down the search space by repeatedly dividing it in half. 
