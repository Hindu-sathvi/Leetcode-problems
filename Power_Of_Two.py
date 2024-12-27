#https://leetcode.com/problems/power-of-two/description/?envType=problem-list-v2&envId=math
#Code:
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
        #without using loops we can convert the given number into binary number
        #After converting the number into binary number we evaluate this function n & (n - 1) which should result into 0 for powers of 2.
        
