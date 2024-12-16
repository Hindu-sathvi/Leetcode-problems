class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            total_coins = (mid * (mid + 1)) // 2  

            if total_coins == n:
                return mid
            elif total_coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right