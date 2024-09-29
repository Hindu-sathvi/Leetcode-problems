#https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=hash-table
#code:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        length = 0
        odd_found = False
        
        for c in count.values():
            if c % 2 == 0:
                length += c 
            else:
                length += c - 1  
                odd_found = True 
    
        if odd_found:
            length += 1
        
        return length

solution = Solution()
s1 = "abccccdd"
print(solution.longestPalindrome(s1)) 

s2 = "a"
print(solution.longestPalindrome(s2))
