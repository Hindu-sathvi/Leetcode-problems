#https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY
#Code:
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
    
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        
