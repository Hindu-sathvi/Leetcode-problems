#https://leetcode.com/problems/remove-outermost-parentheses/?envType=problem-list-v2&envId=stack
#Code:
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        balance = 0

        for char in s:
            if char == '(':
                if balance > 0:
                    result.append(char)
                balance += 1
            elif char == ')':
                balance -= 1
                if balance > 0:
                    result.append(char)

        return "".join(result)
        
