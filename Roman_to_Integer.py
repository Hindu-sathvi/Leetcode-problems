#https://leetcode.com/problems/roman-to-integer/
#Code:
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_val=0
        prev_val=0
        
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        #if s in dict:
        #   return dict[s]
        for char in reversed(s):#as left to right
            val=dict[char]
            if val<prev_val:
                total_val -=val
            else:
                total_val +=val
            prev_val=val
        return total_val
sol=Solution()
print(sol.romanToInt('VI'))