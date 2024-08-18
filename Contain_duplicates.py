#https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dicts = {}  # Create an empty dictionary
        
        for i in range(len(nums)):
            num = nums[i]  # Get the current number.
            
            if num in dicts:  # Check if the number is already in the dictionary.
                if i - dicts[num] <= k:  # Check if the current and previous indices are within k distance.
                    return True  # If they are, return True.
            
            dicts[num] = i  # Update the dictionary
        
        return False 
sol = Solution()
# Example
nums = [1, 2, 3, 1]
result = sol.containsNearbyDuplicate(nums, 3)
print(result)  # Should print True because there are duplicates within distance k
