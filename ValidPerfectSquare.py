#https://leetcode.com/problems/valid-perfect-square/?envType=problem-list-v2&envId=binary-search&difficulty=EASY
#Code:
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
        
