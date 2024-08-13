#https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution:
    def plusOne(self, digits):
        # Start from the end of the list and work backwards
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Reset this digit to 0 and continue the carry
        
        # If all digits are 9, the list would be all zeros now, so prepend 1
        return [1] + digits
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(solution.plusOne([9]))  # Output: [1, 0]
