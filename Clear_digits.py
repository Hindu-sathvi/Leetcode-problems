class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def has_digits(s):
            for char in s:
                if char.isdigit():
                    return True
            return False

        s = list(s) 
        while has_digits(s): 
            for i in range(len(s)):
                if s[i].isdigit():
                    # Remove the digit and the closest non-digit character to its left
                    s.pop(i) 
                    if i > 0:
                        s.pop(i - 1) 
                    break 
        return ''.join(s)
solution = Solution()
print(solution.clearDigits("cb34"))  
