#https://leetcode.com/problems/prime-in-diagonal/description/?envType=problem-list-v2&envId=matrix&difficulty=EASY
#Code:
class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def is_prime(n):
            if n <= 1:  
                return False
            for i in range(2, n): 
                if n % i == 0: 
                    return False
            return True  


        n = len(nums)  
        max_prime = 0  
        for i in range(n):
            if is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                max_prime = max(max_prime, nums[i][n - i - 1])

        return max_prime

        
