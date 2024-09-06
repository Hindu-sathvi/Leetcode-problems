#https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue
#code:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for index in range(len(s)):
            char = s[index] 
            if char_count[char] == 1:
                return index 

        return -1
solution = Solution()
print(solution.firstUniqChar("leetcode"))     
print(solution.firstUniqChar("loveleetcode"))  
print(solution.firstUniqChar("aabb"))         
