#https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150
#code:
class Solution:
    def trailingZeroes(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count