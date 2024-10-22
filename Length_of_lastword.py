#https://leetcode.com/problems/length-of-last-word/description/
#1.Code:
#This approach is where we remove any spaces from rside of side using rstrip  and form right if we encounter any space then we return the length 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        s = s.rstrip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ': 
                break
            length += 1

        return length
sol=Solution()
print(sol.lengthOfLastWord)
#2.Code:
#in this approach we get the last word of a string and find the length of it
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        return len(words[-1])
sol=Solution()
print(sol.lengthOfLastWord)
