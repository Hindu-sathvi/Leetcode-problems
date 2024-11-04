#https://leetcode.com/problems/longest-nice-substring/?envType=problem-list-v2&envId=divide-and-conquer
#Code:
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        result = ""
        for length in range(len(s), 1, -1):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]

                if is_nice(substring):
                    if length > max_len:
                        max_len = length
                        result = substring
                    break  
    
        return result

def is_nice(subs):
    lower = set(c for c in subs if c.islower())
    upper = set(c for c in subs if c.isupper())
    return all(c.upper() in upper for c in lower) and all(c.lower() in lower for c in upper)
        