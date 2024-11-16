#https://leetcode.com/problems/n-th-tribonacci-number/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY
#Code:
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        store={}
        def fibonacci(a):
            if a==0:
                return 0
            elif a==1 or a==2:
                return 1
            if a not in store:
                store[a]=fibonacci(a-1)+fibonacci(a-2)+fibonacci(a-3)
            return store[a]
        return fibonacci(n)
        
