#https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        power=x**n
        return power
sol = Solution()
print(sol.myPow(2,10)) 
print(sol.myPow(2,-2)) 

        