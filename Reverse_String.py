#https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=two-pointers&difficulty=EASY
#Code:
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        fast,slow=len(s)-1,0
        while slow<fast:
            s[slow],s[fast]=s[fast],s[slow]
            slow+=1
            fast-=1
        return s
        
