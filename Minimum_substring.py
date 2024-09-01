#https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
#minimum-string-length-after-removing-substrings
#code:
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
    
        for char in s:
            # Check if the current character and the top of the stack form "AB" or "CD"
            if stack:
                top = stack[-1]  # Get the last character in the stack
                if (top == 'A' and char == 'B') or (top == 'C' and char == 'D'):
                    stack.pop()  # Remove the last character from the stack
                else:
                    stack.append(char)  # Add the current character to the stack
            else:
                stack.append(char)  # If the stack is empty, add the current character

        # The remaining characters in the stack form the minimized string
        return len(stack)
sol = Solution()
print(sol.minLength("ABFCACDB")) 
print(sol.minLength("ACBBD"))     
