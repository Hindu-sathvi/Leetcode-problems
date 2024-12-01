#https://leetcode.com/problems/defuse-the-bomb/description/?envType=problem-list-v2&envId=sliding-window&difficulty=EASY
#Code:
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
    
        if k == 0:
            return [0] * n

        result = [0] * n
        window_sum = 0
        start, end = (1, k) if k > 0 else (n + k, n - 1)
    

        for i in range(start, end + 1):
            window_sum += code[i % n]

        for i in range(n):
            result[i] = window_sum
        
            window_sum -= code[start % n]
            start += 1
            end += 1
            window_sum += code[end % n]
    
        return result
        
