#https://leetcode.com/problems/find-the-difference/?envType=problem-list-v2&envId=string
#Code:
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for char in t:
            if t.count(char) > s.count(char):
                return char
        
