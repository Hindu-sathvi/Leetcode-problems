#https://leetcode.com/problems/fibonacci-number/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=EASY
#Code:
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        store={}
        def fibonacci(a):
            if a<=1:
                return a
            if a not in store:
                store[a]=fibonacci(a-1)+fibonacci(a-2)
            return store[a]
        return fibonacci(n)
