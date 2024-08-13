#https://leetcode.com/problems/palindrome-number/submissions/1354433867/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution:
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_number = 0
        original = x
        # Reversing half of the number
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        # Check if the number is the same as its reverse
        return x == reversed_number or x == reversed_number // 10
