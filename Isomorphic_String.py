#https://leetcode.com/problems/isomorphic-strings/?envType=problem-list-v2&envId=string
#Code:
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def get_pattern(string):
            pattern = {}
            pattern_list = []
            for char in string:
                if char not in pattern:
                    pattern[char] = len(pattern)
                pattern_list.append(pattern[char])
            return pattern_list
    
        return get_pattern(s) == get_pattern(t)
#Here we a generate a pattern for the string s and string t and compare the patterns.If the patterns are same we return true.
