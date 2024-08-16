#https://leetcode.com/problems/happy-number/submissions/1357959696/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
       
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10  # Get the last digit
                total_sum += digit ** 2  # Square it and add to the total sum
                number //= 10  # Remove the last digit
            return total_sum

        seen_numbers = set()
        
        while True:
            if n == 1:
                return True
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
            n = get_next(n)

sol = Solution()
print(sol.isHappy(19)) 
print(sol.isHappy(2))   
