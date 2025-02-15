#https://leetcode.com/problems/valid-palindrome/
#Code:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palin = ""
        for char in s:
            if char.isalnum():
                palin += char.lower()
        return palin == palin[::-1]
        
